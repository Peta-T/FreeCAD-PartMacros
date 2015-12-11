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
directory =LIBRARYPATH+'/Mechanical Parts/Profiles EN/DIN1025-4 HE-M-Profiles/'
if not os.path.exists(directory):
    os.mkdir(directory)

Table = (
         ("HE-M-Profile 100 DIN1025-4 S235JR",	120.00,	106.00,	12.00,	20.00,	12.00),
         ("HE-M-Profile 120 DIN1025-4 S235JR",	140.00,	126.00,	12.50,	21.00,	12.00),
         ("HE-M-Profile 140 DIN1025-4 S235JR",	160.00,	146.00,	13.00,	22.00,	12.00),
         ("HE-M-Profile 160 DIN1025-4 S235JR",	180.00,	166.00,	14.00,	23.00,	15.00),
         ("HE-M-Profile 180 DIN1025-4 S235JR",	200.00,	186.00,	14.50,	24.00,	15.00),
         ("HE-M-Profile 200 DIN1025-4 S235JR",	220.00,	206.00,	15.00,	25.00,	18.00),
         ("HE-M-Profile 220 DIN1025-4 S235JR",	240.00,	226.00,	15.50,	26.00,	18.00),
         ("HE-M-Profile 240 DIN1025-4 S235JR",	270.00,	248.00,	18.00,	32.00,	21.00),
         ("HE-M-Profile 260 DIN1025-4 S235JR",	290.00,	268.00,	18.00,	32.50,	24.00),
         ("HE-M-Profile 280 DIN1025-4 S235JR",	310.00,	288.00,	18.50,	33.00,	24.00),
         ("HE-M-Profile 300 DIN1025-4 S235JR",	340.00,	310.00,	21.00,	39.00,	27.00),
         ("HE-M-Profile 320x305 DIN1025-4 S235JR",	320.00,	305.00,	16.00,	29.00,	27.00),
         ("HE-M-Profile 320 DIN1025-4 S235JR",	359.00,	309.00,	21.00,	40.00,	27.00),
         ("HE-M-Profile 340 DIN1025-4 S235JR",	377.00,	309.00,	21.00,	40.00,	27.00),
         ("HE-M-Profile 360 DIN1025-4 S235JR",	395.00,	308.00,	21.00,	40.00,	27.00),
         ("HE-M-Profile 400 DIN1025-4 S235JR",	432.00,	307.00,	21.00,	40.00,	27.00),
         ("HE-M-Profile 450 DIN1025-4 S235JR",	478.00,	307.00,	21.00,	40.00,	27.00),
         ("HE-M-Profile 500 DIN1025-4 S235JR",	524.00,	306.00,	21.00,	40.00,	27.00),
         ("HE-M-Profile 550 DIN1025-4 S235JR",	572.00,	306.00,	21.00,	40.00,	27.00),
         ("HE-M-Profile 600 DIN1025-4 S235JR",	620.00,	305.00,	21.00,	40.00,	27.00),
         ("HE-M-Profile 650 DIN1025-4 S235JR",	668.00,	305.00,	21.00,	40.00,	27.00),
         ("HE-M-Profile 700 DIN1025-4 S235JR",	716.00,	304.00,	21.00,	40.00,	27.00),
         ("HE-M-Profile 800 DIN1025-4 S235JR",	814.00,	303.00,	21.00,	40.00,	30.00),
         ("HE-M-Profile 900 DIN1025-4 S235JR",	910.00,	302.00,	21.00,	40.00,	30.00),
         ("HE-M-Profile 1000 DIN1025-4 S235JR",	1008.0,	302.00,	21.00,	40.00,	30.00))




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

 

 
 

