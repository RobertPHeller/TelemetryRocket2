#!/usr/local/bin/FreeCAD018                                                     
#*****************************************************************************
#
#  System        : 
#  Module        : 
#  Object Name   : $RCSfile$
#  Revision      : $Revision$
#  Date          : $Date$
#  Author        : $Author$
#  Created By    : Robert Heller
#  Created       : Sat Aug 8 08:47:22 2020
#  Last Modified : <200808.1935>
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

class NoseCone(object):
    _hstep = .125
    _rfract = .975
    def __init__(self,name,origin,size='BT-50',height=30,\
                    color=tuple([1.0,1.0,0.0])):
        self.name = name
        if not isinstance(origin,Base.Vector):
            raise RuntimeError("origin is not a Vector!")
        self.origin = origin
        self.color = color
        if size in BodyTube._bodysizes:
            radius = BodyTube._bodysizes[size]
        else:
            raise RuntimeError("Undefined body size!")
        h = height
        r = radius
        cone = None
        bottom = origin
        while (r > 0.0001) and (h > 0.0001):
            #print("*** NoseCone.__init__():bottom.z = ",bottom.z,file=sys.__stderr__)
            #print("*** NoseCone.__init__():r = ",r,", h = ",h,file=sys.__stderr__)
            h1 = h * self._hstep
            #print("*** NoseCone.__init__():h1 = ",h1,file=sys.__stderr__)
            hvect = Base.Vector(0,0,h1)
            r1 = r * self._rfract
            #print("*** NoseCone.__init__():r1 = ",r1,file=sys.__stderr__)
            basedisk = Part.Face(Part.Wire(Part.makeCircle(r,bottom)))
            c1 = basedisk.extrude(hvect)
            if cone == None:
                cone = c1
            else:
                cone = cone.fuse(c1)
            r = r1
            bottom = bottom.add(hvect)
            h -= h1
        self.cone = cone.fuse(Part.Face(Part.Wire(Part.makeCircle(radius-.5,origin))).extrude(Base.Vector(0,0,-12.5)))
    def show(self):
        doc = App.activeDocument()
        obj = doc.addObject("Part::Feature",self.name)
        obj.Shape = self.cone
        obj.Label=self.name
        obj.ViewObject.ShapeColor=self.color
        

if __name__ == '__main__':
    doc = App.newDocument("TestCone")
    App.setActiveDocument ("TestCone")
    o = Base.Vector(0,0,0)
    cone = NoseCone("test",o)
    cone.show()
    Gui.SendMsgToActiveView("ViewFit")
