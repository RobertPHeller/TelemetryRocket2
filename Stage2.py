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
#  Created       : Sat Aug 8 16:54:54 2020
#  Last Modified : <200808.1725>
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



class Stage2(object):
    def __init__(self,name,origin):
        self.name = name
        if not isinstance(origin,Base.Vector):
            raise RuntimeError("origin is not a Vector!")
        self.origin = origin
        self.center = Engine(name+"_center",origin,size='E24')
        self.centermount = BodyTube(name+"_centermount",\
                                    origin.add(Base.Vector(0,0,6.35)),\
                                    size='BT-50',length=95)
        self.centermountlowerring = EngineMountRing(\
                    name+"_centermountlowerring",\
                    origin.add(Base.Vector(0,0,50.8-(95-(70 + 6.35))+6.35)),\
                    enginesize='E24',tubesize='BT-55')
        self.centermountupperring = EngineMountRing(\
                    name+"_centermountlowerring",\
                    origin.add(Base.Vector(0,0,95)),\
                    enginesize='E24',tubesize='BT-55')
        self.stage2 = BodyTube(name+"_stage2",\
                               origin.add(Base.Vector(0,0,6.35)),\
                               size='BT-55',length=400)
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
        self.centermountlowerring.show()
        self.centermountupperring.show()
        self.stage2.show()
        self.fin1.show()
        self.fin2.show()
        self.fin3.show()

if __name__ == '__main__':
    doc = App.newDocument("Stage2")
    App.setActiveDocument ("Stage2")
    o = Base.Vector(0,0,0)
    stage2 = Stage2("stage2",o)
    stage2.show()
    Gui.SendMsgToActiveView("ViewFit")

