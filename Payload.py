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
#  Created       : Sat Aug 8 19:33:35 2020
#  Last Modified : <200810.1004>
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
from NoseCone import *
from ComputerAssembly import *



class Payload(object):
    def __init__(self,name,origin,transparency=0):
        self.name = name
        if not isinstance(origin,Base.Vector):
            raise RuntimeError("origin is not a Vector!")
        self.origin = origin
        self.transparency = transparency
        self.tube = BodyTube(name+"_tube",origin,size='BT-55',\
                             length=25.4+ComputerAssembly._boardLength,\
                             transparency=transparency)
        self.computerAssembly = ComputerAssembly(name+"_computerAssembly",\
                                origin.add(Base.Vector(0,0,12.5)))
        self.coupler = Part.Face(Part.Wire(Part.makeCircle(BodyTube._bodysizes['BT-55']-.5,origin.add(Base.Vector(0,0,-12.5))))).extrude(Base.Vector(0,0,25.4))
        self.cone    = NoseCone(name+"_cone",origin.add(Base.Vector(0,0,25.4+ComputerAssembly._boardLength)),size='BT-55',height=50)
    def show(self):
        self.tube.show()
        self.cone.show()
        self.computerAssembly.show()
        doc = App.activeDocument()
        obj = doc.addObject("Part::Feature",self.name+"_coupler")
        obj.Shape = self.coupler
        obj.Label=self.name+"_coupler"
        obj.ViewObject.ShapeColor=tuple([1.0,1.0,0.0])
        


if __name__ == '__main__':
    doc = App.newDocument("Payload")
    App.setActiveDocument ( "Payload" )
    o = Base.Vector(0,0,0)
    payload = Payload("Payload",o,transparency=50)
    payload.show()
    Gui.SendMsgToActiveView("ViewFit")
