#*****************************************************************************
#
#  System        : 
#  Module        : 
#  Object Name   : $RCSfile$
#  Revision      : $Revision$
#  Date          : $Date$
#  Author        : $Author$
#  Created By    : Robert Heller
#  Created       : Sat Aug 8 08:47:00 2020
#  Last Modified : <200808.1950>
#
#  Description	
#
#  Notes
#
#  History
#	
#*****************************************************************************
#
#    Copyright (C) 2020  Robert Heller D/B/A Deepwoods Software
#			51 Locke Hill Road
#			Wendell, MA 01379-9728
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#
# 
#
#*****************************************************************************



import FreeCAD as App
import Part
from FreeCAD import Base

import os
import sys
sys.path.append(os.path.dirname(__file__))

from abc import ABCMeta, abstractmethod, abstractproperty

class BodyTube(object):
    _bodysizes = {
        'BT-5'  : 7,
        'BT-20' : 9.5,
        'BT-50' : 12.5,
        'BT-55' : 17,
        'BT-60' : 21,
        'BT-80' : 33
    }
    def __init__(self,name,origin,size='BT-5',length=457,\
                 color=tuple([210.0/255.0,180.0/255.0,140.0/255.0]),\
                 transparency=0):
        self.name = name
        if not isinstance(origin,Base.Vector):
            raise RuntimeError("origin is not a Vector!")
        self.origin = origin
        self.color = color
        self.transparency = transparency
        if size in self._bodysizes:
            radius = self._bodysizes[size]
        else:
            raise RuntimeError("Undefined body size!")
        self.tube = Part.Face(Part.Wire(Part.makeCircle(radius,origin))).extrude(Base.Vector(0,0,length))
        self.tube = self.tube.cut(Part.Face(Part.Wire(Part.makeCircle(radius-.5,origin))).extrude(Base.Vector(0,0,length)))
    def show(self):
        doc = App.activeDocument()
        obj = doc.addObject("Part::Feature",self.name)
        obj.Shape = self.tube
        obj.Label=self.name
        obj.ViewObject.ShapeColor=self.color
        obj.ViewObject.Transparency=self.transparency
        
