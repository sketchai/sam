#!/usr/bin/env python

import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()

###
### SHAPER component
###

from salome.shaper import model

model.begin()
partSet = model.moduleDocument()

### Create Part
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()

### Create Sketch
Sketch_1 = model.addSketch(Part_1_doc, model.defaultPlane("XOY"))

### Create SketchProjection
SketchProjection_0 = Sketch_1.addProjection(model.selection("VERTEX", "PartSet/Origin"), False)
SketchPoint_0 = SketchProjection_0.createdFeature()
SketchLine_0 = Sketch_1.addLine(11,22,33,44)
SketchCircle_1 = Sketch_1.addCircle(0.0,5.0,1)

model.do()
model.end()
###
### SHAPERSTUDY component
###
if salome.sg.hasDesktop():
    salome.sg.updateObjBrowser()