# -*- coding:utf-8 -*-
#***************************************************************************
#*                                                                         *
#*   Copyright (c) 2015 Peta-T          <petaemail@seznam.cz>              *
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU Lesser General Public License (LGPL)    *
#*   as published by the Free Software Foundation; either version 2 of     *
#*   the License, or (at your option) any later version.                   *
#*   for detail see the LICENCE text file.                                 *
#*                                                                         *
#*   This program is distributed in the hope that it will be useful,       *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
#*   GNU Library General Public License for more details.                  *
#*                                                                         *
#*   You should have received a copy of the GNU Library General Public     *
#*   License along with this program; if not, write to the Free Software   *
#*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
#*   USA                                                                   *
#*                                                                         *
#***************************************************************************

import FreeCAD, FreeCADGui, Part, Draft, math, MeshPart, Mesh, Drawing
from PyQt4 import QtGui,QtCore
from FreeCAD import Base
from FreeCAD import Vector
import ImportGui
import Mesh
import os

App=FreeCAD
Gui=FreeCADGui

param = FreeCAD.ParamGet('User parameter:Plugins/parts_library')
s=param.GetString('destination')
print('User parameter:Plugins/partlib : destination : ',s)

if s<>'':
    LIBRARYPATH = s
else:
    folderDialog = QtGui.QFileDialog.getExistingDirectory(None,u"Choose folder library")
    param.SetString('destination',str(folderDialog))
    s=param.GetString('destination')
    LIBRARYPATH = s


directory =LIBRARYPATH+'/Mechanical Parts/'
if not os.path.exists(directory):
    os.mkdir(directory)
directory =LIBRARYPATH+'/Mechanical Parts/Profiles EN/'
if not os.path.exists(directory):
    os.mkdir(directory)
directory =LIBRARYPATH+'/Mechanical Parts/Profiles EN/EN10059 Square steel bars/'
if not os.path.exists(directory):
    os.mkdir(directory)

Table = (("Square Bar 8 EN10059 S235JR", 8),
         ("Square Bar 10 EN10059 S235JR", 10),
         ("Square Bar 12 EN10059 S235JR", 12),
         ("Square Bar 14 EN10059 S235JR", 14),
         ("Square Bar 15 EN10059 S235JR", 15),
         ("Square Bar 16 EN10059 S235JR", 16),
         ("Square Bar 18 EN10059 S235JR", 18),
         ("Square Bar 20 EN10059 S235JR", 20),
         ("Square Bar 25 EN10059 S235JR", 25),
         ("Square Bar 30 EN10059 S235JR", 30),
         ("Square Bar 35 EN10059 S235JR", 35),
         ("Square Bar 40 EN10059 S235JR", 40),
         ("Square Bar 45 EN10059 S235JR", 45),
         ("Square Bar 50 EN10059 S235JR", 50),
         ("Square Bar 55 EN10059 S235JR", 55),
         ("Square Bar 60 EN10059 S235JR", 60),
         ("Square Bar 65 EN10059 S235JR", 65),
         ("Square Bar 70 EN10059 S235JR", 70),
         ("Square Bar 75 EN10059 S235JR", 75),
         ("Square Bar 80 EN10059 S235JR", 80),
         ("Square Bar 90 EN10059 S235JR", 90),
         ("Square Bar 100 EN10059 S235JR", 100),
         ("Square Bar 110 EN10059 S235JR", 110),
         ("Square Bar 120 EN10059 S235JR", 120),
         ("Square Bar 125 EN10059 S235JR", 125),
         ("Square Bar 130 EN10059 S235JR", 130),
         ("Square Bar 135 EN10059 S235JR", 135),
         ("Square Bar 140 EN10059 S235JR", 140),
         ("Square Bar 150 EN10059 S235JR", 150),
         ("Square Bar 160 EN10059 S235JR", 160),
         ("Square Bar 170 EN10059 S235JR", 170),
         ("Square Bar 180 EN10059 S235JR", 180),
         ("Square Bar 200 EN10059 S235JR", 200),
         ("Square Bar 220 EN10059 S235JR", 220),
         ("Square Bar 240 EN10059 S235JR", 240))


for data in Table:
    print data[0]
    doc=FreeCAD.newDocument("Bar")
    sk1=doc.addObject('Sketcher::SketchObject','Sketch')
    sk1.Placement = App.Placement(App.Vector(0.000000,0.000000,0.000000),App.Rotation  (0.000000,0.000000,0.000000,1.000000))

    sk1.addGeometry(Part.Line(App.Vector(-10.000000,-10.000000,0),App.Vector(10.000000,-10.000000,0)))
    sk1.addGeometry(Part.Line(App.Vector(10.000000,-10.000000,0),App.Vector(10.000000,10.000000,0)))
    sk1.addGeometry(Part.Line(App.Vector(10.000000,10.000000,0),App.Vector(-10.000000,10.000000,0)))
    sk1.addGeometry(Part.Line(App.Vector(-10.000000,10.000000,0),App.Vector(-10.000000,-10.000000,0)))
    sk1.addConstraint(Sketcher.Constraint('Coincident',0,2,1,1)) 
    sk1.addConstraint(Sketcher.Constraint('Coincident',1,2,2,1)) 
    sk1.addConstraint(Sketcher.Constraint('Coincident',2,2,3,1)) 
    sk1.addConstraint(Sketcher.Constraint('Coincident',3,2,0,1)) 
    sk1.addConstraint(Sketcher.Constraint('Horizontal',0)) 
    sk1.addConstraint(Sketcher.Constraint('Horizontal',2)) 
    sk1.addConstraint(Sketcher.Constraint('Vertical',1)) 
    sk1.addConstraint(Sketcher.Constraint('Vertical',3)) 
    sk1.addConstraint(Sketcher.Constraint('Symmetric',1,2,0,2,-1)) 
    sk1.addConstraint(Sketcher.Constraint('Symmetric',2,2,1,2,-2)) 
    sk1.addConstraint(Sketcher.Constraint('Equal',1,2)) 
    sk1.addConstraint(Sketcher.Constraint('DistanceY',1,20.000000)) 
    sk1.setDatum(11,App.Units.Quantity(str(data[1])+' mm'))

    myEx=App.ActiveDocument.addObject("Part::Extrusion","Extrude")
    myEx.Base = sk1
    myEx.Dir = (0,0,50)
    myEx.Solid = (True)
    myEx.TaperAngle = (0)
    myEx.Label = data[0]

    FreeCADGui.getDocument(App.ActiveDocument.Name).getObject("Extrude").LineColor = (0.0,0.0,0.0)
    FreeCADGui.getDocument(App.ActiveDocument.Name).getObject("Extrude").ShapeColor = (0.96,0.93,0.76)

    Gui.getDocument(App.ActiveDocument.Name).getObject("Sketch").Visibility=False
    App.ActiveDocument.recompute()
    Gui.SendMsgToActiveView("ViewFit")

    App.ActiveDocument.saveAs(directory+data[0]+'.FCStd')
    __objs__=[]
    __objs__.append(FreeCAD.getDocument(App.ActiveDocument.Name).getObject("Extrude"))
    ImportGui.export(__objs__,directory+data[0]+'.step')
    Mesh.export(__objs__,directory+data[0]+'.stl')
    del __objs__
    App.closeDocument(App.ActiveDocument.Name)

print 'End'

 

 
 

