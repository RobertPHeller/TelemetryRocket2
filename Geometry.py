#*****************************************************************************
#
#  System        : 
#  Module        : 
#  Object Name   : $RCSfile$
#  Revision      : $Revision$
#  Date          : $Date$
#  Author        : $Author$
#  Created By    : Robert Heller
#  Created       : Sat Aug 8 10:27:28 2020
#  Last Modified : <200808.1618>
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

from FreeCAD import Base

import numpy as np

from math import *

def radians(degrees):
    return (degrees/180.0)*pi
    
def pointXdeltaatang(angle,dx=25,z=0):
    theta = radians(angle)
    return Base.Vector(sin(theta)*dx,cos(theta)*dx,z)
    
def rotateZAxis(pointsH, theta_rads):
    pointsMat = np.array(pointsH)    
    n,p = pointsMat.shape
    rmat = np.array( [ [cos(theta_rads), -sin(theta_rads), 0, 0], \
                    [sin(theta_rads),  cos(theta_rads), 0, 0], \
                    [              0,                0, 1, 0], \
                    [              0,                0, 0, 1] ] )
    m = p
    resultMat = np.zeros_like(pointsMat)
    for i in range(n):
        for j in range(p):
            resultMat[i,j] = 0.0
            for k in range(m):
                p1 = pointsMat[i,k]*rmat[j,k]
                p2 = resultMat[i,j]
                resultMat[i,j] = p2+p1
                
    return(resultMat.tolist())
    
def translate3D(pointsH, vector3D):
    pointsMat = np.array(pointsH)
    n,p = pointsMat.shape
    resultMat = np.zeros_like(pointsMat)
    for i in range(n):
        resultMat[i,0] = pointsMat[i,0] + vector3D.x
        resultMat[i,1] = pointsMat[i,1] + vector3D.y
        resultMat[i,2] = pointsMat[i,2] + vector3D.z
        resultMat[i,3] = pointsMat[i,3]
    return(resultMat.tolist())
    

def vectorListFromPointsH(pointsH):
    result = list()
    for p in pointsH:
        result.append(Base.Vector(p[0],p[1],p[2]))
    return result
    
