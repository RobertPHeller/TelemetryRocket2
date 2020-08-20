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
#  Created       : Sat Aug 8 08:25:23 2020
#  Last Modified : <200810.1015>
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

from Stage1 import *
from Stage2 import *
from Payload import *

class CompleteRocket(object):
    def __init__(self,name,origin):
        self.name = name
        if not isinstance(origin,Base.Vector):
            raise RuntimeError("origin is not a Vector!")
        self.origin = origin
        self.stage1 = Stage1(name+"_Stage1",origin)
        self.stage2 = Stage2(name+"_Stage2",origin.add(Base.Vector(0,0,95)))
        self.payload = Payload(name+"_Payload",\
                                origin.add(Base.Vector(0,0,95+400)), \
                                transparency=50)
    def show(self):
        self.stage1.show()
        self.stage2.show()
        self.payload.show()

if __name__ == '__main__':
    doc = App.newDocument("TelemetryRocket2")
    App.setActiveDocument ( "TelemetryRocket2" )
    o = Base.Vector(0,0,0)
    rocket = CompleteRocket("TelemetryRocket2",o)
    rocket.show()
    Gui.SendMsgToActiveView("ViewFit")
    doc.Label="TelemetryRocket2"
    doc.saveAs(os.path.dirname(__file__)+"TelemetryRocket2.fcstd")
    sys.exit(1)
