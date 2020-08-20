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
#  Created       : Sat Aug 8 08:38:49 2020
#  Last Modified : <200808.1726>
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
from BodyTube import *
from Engine   import *
from NoseCone import *
from Fin      import *



class Stage1(object):
    def __init__(self,name,origin):
        self.name = name
        if not isinstance(origin,Base.Vector):
            raise RuntimeError("origin is not a Vector!")
        self.origin = origin
        self.center = Engine(name+"_center",origin,size='E24')
        self.centermount = BodyTube(name+"_centermount",\
                                    origin.add(Base.Vector(0,0,6.35)),\
                                    size='BT-50',length=95)
        self.stagetube = BodyTube(name+"_stagetube",\
                                    origin.add(Base.Vector(0,0,6.35)),\
                                    size='BT-55',length=95)
        self.centermountlowerring = EngineMountRing(\
                name+"_centermountlowerring",\
                origin.add(Base.Vector(0,0,6.35)),\
                enginesize='E24',tubesize='BT-55')
        self.centermountupperring = EngineMountRing(\
                name+"_centermountlowerring",\
                origin.add(Base.Vector(0,0,70)),\
                enginesize='E24',tubesize='BT-55')
        s1origin = origin.add(Geometry.pointXdeltaatang(0,12.5+17,0))
        self.s1 = Engine(name+"_s1Engine",s1origin,size='D')
        self.s1mount = BodyTube(name+"_s1Mount",\
                                s1origin.add(Base.Vector(0,0,6.35)),
                                size='BT-50',length=2*95)
        self.s1cone = NoseCone(name+"_s1cone",\
                                s1origin.add(Base.Vector(0,0,6.35+2*95)),\
                                size='BT-50',height=30)
        s2origin = origin.add(Geometry.pointXdeltaatang(120,12.5+17,0))
        self.s2 = Engine(name+"_s2Engine",s2origin,size='D')
        self.s2mount = BodyTube(name+"_s2Mount",\
                                s2origin.add(Base.Vector(0,0,6.35)),
                                size='BT-50',length=2*95)
        self.s2cone = NoseCone(name+"_s2cone",\
                                s2origin.add(Base.Vector(0,0,6.35+2*95)),\
                                size='BT-50',height=30)
        s3origin = origin.add(Geometry.pointXdeltaatang(240,12.5+17,0))
        self.s3 = Engine(name+"_s3Engine",s3origin,size='D')
        self.s3mount = BodyTube(name+"_s3Mount",\
                                s3origin.add(Base.Vector(0,0,6.35)),
                                size='BT-50',length=2*95)
        self.s3cone = NoseCone(name+"_s3cone",\
                                s3origin.add(Base.Vector(0,0,6.35+2*95)),\
                                size='BT-50',height=30)
        couplerOrig = origin.add(Base.Vector(0,0,70 + 6.35))
        couplerExtrude = Base.Vector(0,0,50.8)
        self.stage1coupler = Part.Face(Part.Wire(Part.makeCircle(33.0/2.0,\
                                       couplerOrig))).extrude(couplerExtrude)
        couplerCut = Part.Face(Part.Wire(Part.makeCircle(31/2.0,\
                                         couplerOrig))).extrude(couplerExtrude)
        self.stage1coupler = self.stage1coupler.cut(couplerCut)
        self.fin1 = FinType1(self.name+"_fin1",\
                             origin.add(Geometry.pointXdeltaatang(60,17,6.35+70)),\
                             orient=60,height=70,angle=30,length=200)
        self.fin2 = FinType1(self.name+"_fin2",\
                             origin.add(Geometry.pointXdeltaatang(180,17,6.35+70)),\
                             orient=180,height=70,angle=30,length=200)
        self.fin3 = FinType1(self.name+"_fin3",\
                             origin.add(Geometry.pointXdeltaatang(300,17,6.35+70)),\
                             orient=300,height=70,angle=30,length=200)
    def show(self):
        self.center.show()
        self.centermount.show()
        self.stagetube.show()
        self.centermountlowerring.show()
        self.centermountupperring.show()
        self.s1.show()
        self.s1mount.show()
        self.s1cone.show()
        self.s2.show()
        self.s2mount.show()
        self.s2cone.show()
        self.s3.show()
        self.s3mount.show()
        self.s3cone.show()
        doc = App.activeDocument()
        obj = doc.addObject("Part::Feature",self.name+"_stage1coupler")
        obj.Shape = self.stage1coupler
        obj.Label=self.name+"_stage1coupler"
        obj.ViewObject.ShapeColor=tuple([1.0,.5,.25])
        self.fin1.show()
        self.fin2.show()
        self.fin3.show()

if __name__ == '__main__':
    doc = App.newDocument("Stage1")
    App.setActiveDocument ( "Stage1")
    o = Base.Vector(0,0,0)
    stage1 = Stage1("stage1",o)
    stage1.show()
    Gui.SendMsgToActiveView("ViewFit")
