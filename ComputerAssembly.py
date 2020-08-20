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
#  Created       : Sat Aug 8 20:11:35 2020
#  Last Modified : <200810.0959>
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

import Geometry

class ComputerAssembly(object):
    _boardLength = 177.8
    _boardWidth  =  33.0
    _boardThick  =   1.6
    def __init__(self,name,origin):
        self.name = name
        if not isinstance(origin,Base.Vector):
            raise RuntimeError("origin is not a Vector!")
        self.origin = origin
        XNorm = Base.Vector(1,0,0)
        BoardExtrude =  Base.Vector(self._boardThick,0,0)
        boardCorner  =  origin.add(Base.Vector(-self._boardThick/2.0,\
                                               self._boardWidth/2.0,\
                                               0))
        #print("*** ComputerAssembly(): origin is ",origin.x,origin.y,origin.z,file=sys.__stderr__)
        #print("*** ComputerAssembly(): boardCorner is ",boardCorner.x,boardCorner.y,boardCorner.z,file=sys.__stderr__)
        self.telemetrypcb = Part.makePlane(self._boardLength,self._boardWidth,boardCorner,XNorm).extrude(BoardExtrude)
        ttgocp = boardCorner.add(Base.Vector(5.08,-3.81,128.27))
        self.ttgo = Part.makePlane(45.72,25.4,ttgocp,XNorm).extrude(BoardExtrude)
        adxl345cp = boardCorner.add(Base.Vector(5.08,-5.08,92.71))
        self.adafruit_adxl345 = Part.makePlane(25.4,20.32,adxl345cp,XNorm).extrude(BoardExtrude)
        mpl3115a2cp = boardCorner.add(Base.Vector(5.08,-5.08,68.5))
        self.adafruit_mpl3115a2 = Part.makePlane(20.32,17.7,mpl3115a2cp,XNorm).extrude(BoardExtrude)
        DS3231_rtccp = boardCorner.add(Base.Vector(5.08,-5.08,40.54))
        self.adafruit_DS3231_rtc = Part.makePlane(22.05,17.7,DS3231_rtccp,XNorm).extrude(BoardExtrude)
        self.topdisk = Part.Face(Part.Wire(Part.makeCircle(33.0/2,origin.add(Base.Vector(0,0,177.8))))).extrude(Base.Vector(0,0,(1.0/8.0)*25.4))
        gradiusX = 26.5/2
        gbottom = -24.5
        gheight = 177.8+12+37.5
        gradius = (1.0/8.0)*25.4
        self.guide1 = Part.Face(Part.Wire(Part.makeCircle(gradius,origin.add(Geometry.pointXdeltaatang(90,gradiusX,gbottom))))).extrude(Base.Vector(0,0,gheight))
        self.guide2 = Part.Face(Part.Wire(Part.makeCircle(gradius,origin.add(Geometry.pointXdeltaatang(210,gradiusX,gbottom))))).extrude(Base.Vector(0,0,gheight))
        self.guide3 = Part.Face(Part.Wire(Part.makeCircle(gradius,origin.add(Geometry.pointXdeltaatang(330,gradiusX,gbottom))))).extrude(Base.Vector(0,0,gheight))
    def show(self):
        doc = App.activeDocument()
        obj = doc.addObject("Part::Feature",self.name+"_telemetrypcb")
        obj.Shape = self.telemetrypcb
        obj.Label=self.name+"_telemetrypcb"
        obj.ViewObject.ShapeColor=tuple([0.0,.75,0.0])
        obj = doc.addObject("Part::Feature",self.name+"_ttgo")
        obj.Shape = self.ttgo
        obj.Label=self.name+"_ttgo"
        obj.ViewObject.ShapeColor=tuple([0.0,0.0,0.0])
        obj = doc.addObject("Part::Feature",self.name+"_adafruit_adxl345")
        obj.Shape = self.adafruit_adxl345
        obj.Label=self.name+"_adafruit_adxl345"
        obj.ViewObject.ShapeColor=tuple([0.0,0.0,1.0])
        obj = doc.addObject("Part::Feature",self.name+"_adafruit_mpl3115a2")
        obj.Shape = self.adafruit_mpl3115a2
        obj.Label=self.name+"_adafruit_mpl3115a2"
        obj.ViewObject.ShapeColor=tuple([0.0,0.0,1.0])
        obj = doc.addObject("Part::Feature",self.name+"_adafruit_DS3231_rtc")
        obj.Shape = self.adafruit_DS3231_rtc
        obj.Label=self.name+"_adafruit_DS3231_rtc"
        obj.ViewObject.ShapeColor=tuple([0.0,0.0,1.0])
        obj = doc.addObject("Part::Feature",self.name+"_topdisk")
        obj.Shape = self.topdisk
        obj.Label=self.name+"_topdisk"
        obj.ViewObject.ShapeColor=tuple([1.0,1.0,1.0])
        obj = doc.addObject("Part::Feature",self.name+"_guide1")
        obj.Shape = self.guide1
        obj.Label=self.name+"_guide1"
        obj.ViewObject.ShapeColor=tuple([1.0,1.0,1.0])
        obj = doc.addObject("Part::Feature",self.name+"_guide2")
        obj.Shape = self.guide2
        obj.Label=self.name+"_guide2"
        obj.ViewObject.ShapeColor=tuple([1.0,1.0,1.0])
        obj = doc.addObject("Part::Feature",self.name+"_guide3")
        obj.Shape = self.guide3
        obj.Label=self.name+"_guide3"
        obj.ViewObject.ShapeColor=tuple([1.0,1.0,1.0])

if __name__ == '__main__':
    doc = App.newDocument("ComputerAssembly")
    App.setActiveDocument("ComputerAssembly")
    o = Base.Vector(0,0,0)
    ca = ComputerAssembly("CA",o)
    ca.show()
    Gui.SendMsgToActiveView("ViewFit")
