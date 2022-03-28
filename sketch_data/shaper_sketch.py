from typing import List
import pickle
import matplotlib.pyplot as plt

from sketch_data.sketch import Sketch
from sketch_data.primitive import Primitive, PrimitiveType
from sketch_data.constraint import Constraint

class ShaperGeometryGeneration():

    @staticmethod
    def headCode():
        head_code = '''#!/usr/bin/env python

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
'''
        return head_code

    @staticmethod
    def tailCode():
        tail_code = '''
model.do()
model.end()
###
### SHAPERSTUDY component
###
if salome.sg.hasDesktop():
    salome.sg.updateObjBrowser()'''

        return tail_code

    @staticmethod
    def export(i,elt):
        if elt.type == PrimitiveType.LINE:
            return ShaperGeometryGeneration().generateLine(i,elt)
        elif elt.type == PrimitiveType.CIRCLE:
            return ShaperGeometryGeneration().generateCircle(i,elt)
        else:
            return None
            
    @staticmethod
    def generateLine(i,elt):
        """Returns the python code corresponding to the creation of the current line instance in Shaper"""
        obj = "SketchLine_{}".format(i)
        shaperCode = obj + " = Sketch_1.addLine("+str(elt.pnt1_X)+","+str(elt.pnt1_Y)+"," \
                                                     +str(elt.pnt2_X)+","+str(elt.pnt2_Y)+")\n"
        return shaperCode
    
    @staticmethod
    def generateCircle(i,elt):
        obj = "SketchCircle_{}".format(i)
        shaperCode = obj + " = Sketch_1.addCircle("+str(elt.x_center)+","+str(elt.y_center)+","+str(elt.radius)+")\n"
        return shaperCode


class ShaperConversion(Sketch):

    # def __init__(self):
    #      super().__init__()

    def export(self, out_path: str):
        """export vers le format python Shaper"""
        with open(out_path, 'wt') as f:
            f.write(ShaperGeometryGeneration.headCode())
            for i,elt in enumerate(self.sequence):
                f.write(ShaperGeometryGeneration.export(i,elt))
            f.write(ShaperGeometryGeneration.tailCode())
        f.close()

    def import_file(pythonShaperFile: str) -> Sketch:
    #     """Read a python Shaper file and convert it to sequences of the Skeztch class"""
        pass;    