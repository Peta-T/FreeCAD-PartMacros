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
    param.SetString('destination',folderDialog)
    s=param.GetString('destination')
    LIBRARYPATH = s

directory =LIBRARYPATH+'/Mechanical Parts/'
if not os.path.exists(directory):
    os.mkdir(directory)
directory =LIBRARYPATH+'/Mechanical Parts/Profiles EN/'
if not os.path.exists(directory):
    os.mkdir(directory)
directory =LIBRARYPATH+'/Mechanical Parts/Profiles EN/DIN1025-5 IPE-Profiles/'
if not os.path.exists(directory):
    os.mkdir(directory)

Table = (
         ("IPE-Profile 80 DIN1025-5 S235JR",	80.00,	46.00,	3.80,	5.20,	5.00,	59.60),
         ("IPE-Profile 100 DIN1025-5 S235JR",	100.00,	55.00,	4.10,	5.70,	7.00,	74.60),
         ("IPE-Profile 120 DIN1025-5 S235JR",	120.00,	64.00,	4.40,	6.30,	7.00,	93.40),
         ("IPE-Profile 140 DIN1025-5 S235JR",	140.00,	73.00,	4.70,	6.90,	7.00,	112.20),
         ("IPE-Profile 160 DIN1025-5 S235JR",	160.00,	82.00,	5.00,	7.40,	9.00,	127.20),
         ("IPE-Profile 180 DIN1025-5 S235JR",	180.00,	91.00,	5.30,	8.00,	9.00,	146.00),
         ("IPE-Profile 200 DIN1025-5 S235JR",	200.00,	100.00,	5.60,	8.50,	12.00,	159.00),
         ("IPE-Profile 220 DIN1025-5 S235JR",	220.00,	110.00,	5.90,	9.20,	12.00,	177.60),
         ("IPE-Profile 240 DIN1025-5 S235JR",	240.00,	120.00,	6.20,	9.80,	15.00,	190.40),
         ("IPE-Profile 270 DIN1025-5 S235JR",	270.00,	135.00,	6.60,	10.20,	15.00,	219.60),
         ("IPE-Profile 300 DIN1025-5 S235JR",	300.00,	150.00,	7.10,	10.70,	15.00,	248.60),
         ("IPE-Profile 330 DIN1025-5 S235JR",	330.00,	160.00,	7.50,	11.50,	18.00,	271.00),
         ("IPE-Profile 360 DIN1025-5 S235JR",	360.00,	170.00,	8.00,	12.70,	18.00,	298.60),
         ("IPE-Profile 400 DIN1025-5 S235JR",	400.00,	180.00,	8.60,	13.50,	21.00,	331.00),
         ("IPE-Profile 450 DIN1025-5 S235JR",	450.00,	190.00,	9.40,	14.60,	21.00,	378.80),
         ("IPE-Profile 500 DIN1025-5 S235JR",	500.00,	200.00,	10.20,	16.00,	21.00,	426.00),
         ("IPE-Profile 550 DIN1025-5 S235JR",	550.00,	210.00,	11.10,	17.20,	24.00,	467.60),
         ("IPE-Profile 600 DIN1025-5 S235JR",	600.00,	220.00,	12.00,	19.00,	24.00,	514.00))



for data in Table:
    print data[0]
    doc=FreeCAD.newDocument("Bar")
    sk1=doc.addObject('Sketcher::SketchObject','Sketch')
    sk1.Placement = App.Placement(App.Vector(0.000000,0.000000,0.000000),App.Rotation  (0.000000,0.000000,0.000000,1.000000))

    sk1.addGeometry(Part.Line(App.Vector(1.000000,-2.000000,0),App.Vector(1.000000,2.000000,0)))
    sk1.addConstraint(Sketcher.Constraint('Vertical',0)) 
    sk1.addGeometry(Part.Line(App.Vector(1.000000,2.000000,0),App.Vector(3.000000,2.000000,0)))
    sk1.addConstraint(Sketcher.Constraint('Coincident',1,1,0,2)) 
    sk1.addConstraint(Sketcher.Constraint('Horizontal',1)) 
    sk1.addGeometry(Part.Line(App.Vector(3.000000,2.000000,0),App.Vector(3.000000,3.000000,0)))
    sk1.addConstraint(Sketcher.Constraint('Coincident',2,1,1,2)) 
    sk1.addConstraint(Sketcher.Constraint('Vertical',2)) 
    sk1.addGeometry(Part.Line(App.Vector(3.000000,3.000000,0),App.Vector(-3.000000,3.000000,0)))
    sk1.addConstraint(Sketcher.Constraint('Coincident',3,1,2,2)) 
    sk1.addConstraint(Sketcher.Constraint('Horizontal',3)) 
    sk1.addGeometry(Part.Line(App.Vector(-3.000000,3.000000,0),App.Vector(-3.000000,2.000000,0)))
    sk1.addConstraint(Sketcher.Constraint('Coincident',4,1,3,2)) 
    sk1.addConstraint(Sketcher.Constraint('Vertical',4)) 
    sk1.addGeometry(Part.Line(App.Vector(-3.000000,2.000000,0),App.Vector(-1.000000,2.000000,0)))
    sk1.addConstraint(Sketcher.Constraint('Coincident',5,1,4,2)) 
    sk1.addConstraint(Sketcher.Constraint('Horizontal',5)) 
    sk1.addGeometry(Part.Line(App.Vector(-1.000000,2.000000,0),App.Vector(-1.000000,-2.000000,0)))
    sk1.addConstraint(Sketcher.Constraint('Coincident',6,1,5,2)) 
    sk1.addConstraint(Sketcher.Constraint('Vertical',6)) 
    sk1.addGeometry(Part.Line(App.Vector(-1.000000,-2.000000,0),App.Vector(-3.000000,-2.000000,0)))
    sk1.addConstraint(Sketcher.Constraint('Coincident',7,1,6,2)) 
    sk1.addConstraint(Sketcher.Constraint('Horizontal',7)) 
    sk1.addGeometry(Part.Line(App.Vector(-3.000000,-2.000000,0),App.Vector(-3.000000,-3.000000,0)))
    sk1.addConstraint(Sketcher.Constraint('Coincident',8,1,7,2)) 
    sk1.addConstraint(Sketcher.Constraint('Vertical',8)) 
    sk1.addGeometry(Part.Line(App.Vector(-3.000000,-3.000000,0),App.Vector(3.000000,-3.000000,0)))
    sk1.addConstraint(Sketcher.Constraint('Coincident',9,1,8,2)) 
    sk1.addConstraint(Sketcher.Constraint('Horizontal',9)) 
    sk1.addGeometry(Part.Line(App.Vector(3.000000,-3.000000,0),App.Vector(3.000000,-2.000000,0)))
    sk1.addConstraint(Sketcher.Constraint('Coincident',10,1,9,2)) 
    sk1.addConstraint(Sketcher.Constraint('Vertical',10)) 
    sk1.addGeometry(Part.Line(App.Vector(3.000000,-2.000000,0),App.Vector(1.000000,-2.000000,0)))
    sk1.addConstraint(Sketcher.Constraint('Coincident',11,1,10,2)) 
    sk1.addConstraint(Sketcher.Constraint('Coincident',11,2,0,1)) 
    sk1.addConstraint(Sketcher.Constraint('Horizontal',11)) 
    sk1.fillet(1,0,App.Vector(1.547444,2.000000,0),App.Vector(1.000000,1.666257,0),0.396299)
    sk1.fillet(0,11,App.Vector(1.000000,-1.738673,0),App.Vector(1.392675,-2.000000,0),0.261327)
    sk1.fillet(5,6,App.Vector(-1.304737,2.000000,0),App.Vector(-1.000000,1.577817,0),0.304737)
    sk1.fillet(6,7,App.Vector(-1.000000,-1.252255,0),App.Vector(-1.348957,-2.000000,0),0.529909)
    sk1.addConstraint(Sketcher.Constraint('Equal',3,9)) 
    sk1.addConstraint(Sketcher.Constraint('Equal',2,4)) 
    sk1.addConstraint(Sketcher.Constraint('Equal',4,8)) 
    sk1.addConstraint(Sketcher.Constraint('Equal',8,10)) 
    sk1.addConstraint(Sketcher.Constraint('Equal',12,14)) 
    sk1.addConstraint(Sketcher.Constraint('Equal',14,15)) 
    sk1.addConstraint(Sketcher.Constraint('Equal',15,13)) 
    sk1.addConstraint(Sketcher.Constraint('Symmetric',2,2,3,2,-2)) 
    sk1.addConstraint(Sketcher.Constraint('Symmetric',9,2,8,2,-2)) 
    sk1.addConstraint(Sketcher.Constraint('Symmetric',0,2,6,1,-2)) 
    sk1.addConstraint(Sketcher.Constraint('Symmetric',2,2,9,2,-1)) 
    sk1.addConstraint(Sketcher.Constraint('DistanceY',2,2,9,2,-5.916163)) 
    sk1.setDatum(39,App.Units.Quantity('-5.916160 mm'))
    sk1.addConstraint(Sketcher.Constraint('DistanceX',3,-5.999990)) 
    sk1.setDatum(40,App.Units.Quantity('-5.999990 mm'))
    sk1.addConstraint(Sketcher.Constraint('DistanceX',0,2,6,1,-1.993375)) 
    sk1.setDatum(41,App.Units.Quantity('-1.993370 mm'))
    sk1.addConstraint(Sketcher.Constraint('DistanceY',2,0.964368)) 
    sk1.setDatum(42,App.Units.Quantity('0.964368 mm'))
    sk1.addConstraint(Sketcher.Constraint('Radius',12,0.370847)) 
    sk1.setDatum(43,App.Units.Quantity('0.370847 mm'))
    sk1.delConstraint(5)
    sk1.delConstraint(1)
    sk1.setDatum(37,App.Units.Quantity(str(-data[1])+' mm'))
    sk1.setDatum(38,App.Units.Quantity(str(-data[2])+' mm'))
    sk1.setDatum(39,App.Units.Quantity(str(-data[3])+' mm'))
    sk1.setDatum(40,App.Units.Quantity(str(data[4])+' mm'))
    sk1.setDatum(41,App.Units.Quantity(str(data[5])+' mm'))
    App.ActiveDocument.recompute()

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

 

 
 

