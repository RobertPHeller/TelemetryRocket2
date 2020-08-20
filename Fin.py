#*****************************************************************************
#
#  System        : 
#  Module        : 
#  Object Name   : $RCSfile$
#  Revision      : $Revision$
#  Date          : $Date$
#  Author        : $Author$
#  Created By    : Robert Heller
#  Created       : Sat Aug 8 08:47:31 2020
#  Last Modified : <200808.1648>
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

from math import *
import Geometry                                                                 

class FinType1(object):
    def __init__(self,name,origin,height=70,orient=0,angle=30,length=200,\
                 color=tuple([165.0/255.0,42.0/255.0,42.0/255.0]),thickness=3):
        self.name = name
        if not isinstance(origin,Base.Vector):
            raise RuntimeError("origin is not a Vector!")
        self.origin = origin
        self.color = color
        ang_rads = Geometry.radians(angle)
        rads90   = Geometry.radians(90)
        orads    = Geometry.radians(orient)
        Thick    = Base.Vector(sin(orads)*thickness,cos(orads)*thickness,0)
        #print("*** FinType1(): Thick = ",Thick.x,Thick.y,Thick.z,file=sys.__stderr__)
        polyHomogenous000 = [ \
            [ 0, 0, 0, 1], \
            [ cos(rads90-ang_rads)*length, 0, -(sin(rads90-ang_rads)*length), 1], \
            [ cos(rads90-ang_rads)*length, 0, -(sin(rads90-ang_rads)*length+height), 1], \
            [ 0, 0, -height, 1], \
            [ 0, 0, 0, 1]]
        polyHomogenousRotated = Geometry.rotateZAxis(polyHomogenous000,Geometry.radians(90-orient))
        polyHomogenousToppoint = Geometry.translate3D(polyHomogenousRotated,origin)
        polyVectorList = Geometry.vectorListFromPointsH(polyHomogenousToppoint)
        self.fin = Part.Face(Part.Wire(Part.makePolygon(polyVectorList))).extrude(Thick)
    def show(self):
        doc = App.activeDocument()
        obj = doc.addObject("Part::Feature",self.name)
        obj.Shape = self.fin
        obj.Label=self.name
        obj.ViewObject.ShapeColor=self.color
