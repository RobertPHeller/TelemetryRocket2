#*****************************************************************************
#
#  System        : 
#  Module        : 
#  Object Name   : $RCSfile$
#  Revision      : $Revision$
#  Date          : $Date$
#  Author        : $Author$
#  Created By    : Robert Heller
#  Created       : Sat Aug 8 08:47:12 2020
#  Last Modified : <200808.1038>
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

from BodyTube import *

class Engine(object):
    _enginesizes = {
        'mini'     : (6.5,44),
        'standard' : (9,70),
        'D'        : (12,70),
        'E24'      : (12,95),
        'EF29'     : (14.4,114)
    }
    _enginecolor = tuple([.5,0.0,0.0])
    def __init__(self,name,origin,size='E24'):
        self.name = name
        if not isinstance(origin,Base.Vector):
            raise RuntimeError("origin is not a Vector!")
        self.origin = origin
        if size in self._enginesizes:
            radius,length = self._enginesizes[size]
            self.engine = Part.Face(Part.Wire(Part.makeCircle(radius,origin))).extrude(Base.Vector(0,0,length))
        else:
            raise RuntimeError("Undefined engine size!")
    def show(self):
        doc = App.activeDocument()
        obj = doc.addObject("Part::Feature",self.name)
        obj.Shape = self.engine
        obj.Label=self.name
        obj.ViewObject.ShapeColor=self._enginecolor

class EngineMountRing(object):
    _color = tuple([0.0,.5,0.0])
    def __init__(self,name,origin,enginesize='E24',tubesize='BT-55'):
        self.name = name
        if not isinstance(origin,Base.Vector):
            raise RuntimeError("origin is not a Vector!")
        self.origin = origin
        if enginesize in Engine._enginesizes:
            innerradius,elength = Engine._enginesizes[enginesize]
        else:
            raise RuntimeError("Undefined engine size!")
        if tubesize in BodyTube._bodysizes:
            outerradius = BodyTube._bodysizes[tubesize] - .5
        else:
            raise RuntimeError("Undefined body size!")
        extrudevect = Base.Vector(0,0,6.35)
        self.mount = Part.Face(Part.Wire(Part.makeCircle(outerradius,origin))).extrude(extrudevect)
        self.mount = self.mount.cut(Part.Face(Part.Wire(Part.makeCircle(innerradius,origin))).extrude(extrudevect))
    def show(self):
        doc = App.activeDocument()
        obj = doc.addObject("Part::Feature",self.name)
        obj.Shape = self.mount
        obj.Label=self.name
        obj.ViewObject.ShapeColor=self._color
