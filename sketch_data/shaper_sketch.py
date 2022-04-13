from tkinter import HORIZONTAL
from typing import List
# import pickle, 
import sys
import matplotlib.pyplot as plt
import logging

from sketch_data.sketch import Sketch
from sketch_data.primitive import Primitive, PrimitiveType
from sketch_data.constraint import Constraint, ConstraintType

# sys.path.append("/home/H03832/Donnees/GAN_CAO/gitlab_pleiade/SketchGraphs_For_EDF/sketchgraphs")
# sys.path.append("../../SketchGraphs_For_EDF/sketchgraphs")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

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
        if isinstance(elt,Primitive):
            if elt.type == PrimitiveType.POINT:
                return ShaperGeometryGeneration().generatePoint(i,elt)
            elif elt.type == PrimitiveType.LINE:
                return ShaperGeometryGeneration().generateLine(i,elt)
            elif elt.type == PrimitiveType.CIRCLE:
                return ShaperGeometryGeneration().generateCircle(i,elt)
            elif elt.type == PrimitiveType.ARC:
                return ShaperGeometryGeneration().generateArcOfCircle(i,elt)
            else:
                return "# Primitive "+str(elt)+": this geometry is not implemented.\n"
        elif isinstance(elt,Constraint):
            if elt.type == ConstraintType.HORIZONTAL:
                print(f"{elt.type}")
                return ShaperGeometryGeneration().generateHorizontal(elt)
            elif elt.type == ConstraintType.VERTICAL:
                print(f"{elt.type}")
                return ShaperGeometryGeneration().generateVertical(elt)
            elif elt.type == ConstraintType.PARALLEL:
                print(f"{elt.type}")
                return ShaperGeometryGeneration().generateParallel(elt)
            elif elt.type == ConstraintType.COINCIDENT:
                print(f"{elt.type}")
                return ShaperGeometryGeneration().generateCoincident(elt)
            else:
                return "# Contrainte "+str(elt)+": this constraint is not implemented.\n"
        else:
            print("=========================================================================")
            print(f"{elt}, {elt.type}")
            return None

    @staticmethod
    def generatePoint(i,elt):
        """Returns the python code corresponding to the creation of the current line instance in Shaper"""
        elt.function_name = "SketchPoint_{}".format(i)
        shaperCode = elt.function_name + "= Sketch_1.addPoint({}, {})\n".format(elt.x, elt.y)
        if elt.status_construction:
            shaperCode += elt.function_name + ".setAuxiliary(True)\n".format(i)
        return shaperCode

    @staticmethod
    def generateLine(i,elt):
        """Returns the python code corresponding to the creation of the current line instance in Shaper"""
        elt.function_name = "SketchLine_{}".format(i)
        shaperCode = elt.function_name + " = Sketch_1.addLine("+str(elt.pnt1.x)+","+str(elt.pnt1.y)+"," \
                                                 +str(elt.pnt2.x)+","+str(elt.pnt2.y)+")\n"
        if elt.status_construction:
            shaperCode += elt.function_name + ".setAuxiliary(True)\n".format(i)
        return shaperCode
    
    @staticmethod
    def generateCircle(i,elt):
        elt.function_name = "SketchCircle_{}".format(i)
        shaperCode = elt.function_name + " = Sketch_1.addCircle("+str(elt.x_center)+","+str(elt.y_center)+","+str(elt.radius)+")\n"
        if elt.status_construction:
            shaperCode += obj + ".setAuxiliary(True)\n".format(i)
        return shaperCode

    @staticmethod
    def generateArcOfCircle(i,elt):
        from math import pi as pi, cos as cos, sin as sin
        elt.function_name = "SketchArc_{}".format(i)
        shaperCode = elt.function_name + " = Sketch_1.addArc({}, {}, {}, {}, {}, {}, False)\n". \
            format(
                # Coordinates of the center of the arc :
                elt.x_center, elt.y_center,
                # Cooordinates of the starting point of the arc, located on the circumference :
                elt.x_center+elt.radius*cos(elt.angle_start/180*pi),
                elt.y_center+elt.radius*sin(elt.angle_start/180*pi),
                # Cooordinates of the ending point of the arc, located on the circumference :
                elt.x_center+elt.radius*cos(elt.angle_end/180*pi),
                elt.y_center+elt.radius*sin(elt.angle_end/180*pi)         )
        if elt.status_construction:
            shaperCode += elt.function_name + ".setAuxiliary(True)\n".format(i)
        return shaperCode
    #=================================================================================================================
    # generation of references to geometries that are used in the constraints :
#=================================================================================================================
    @staticmethod
    def generateRefToPoint(name):
        return "{}.coordinates()".format(name)

    @staticmethod
    def generateRefToLine(name):
        return "{}.result()".format(name)

    @staticmethod
    def generateRefToCircle(name):
        return "{}.center()".format(name)

    @staticmethod
    def generateRefToArc(name):
        return "{}.center()".format(name)

    @staticmethod
    def generateRefToGeometry(elt, name):
        logger.info(f'generateRefToGeometry().............')
        if isinstance(elt,Primitive):
            # if '.' in ref:
            #     print("======== subref =========")
            #     i, subref = ref.split('.')
            #     assert i.isdigit()
            #     assert subref.isalpha()
            #     print(ref, subref)
            #     return _CONV_SUBREF_SELON_TYPE.get(entites[i].type)(i, subref)
            # else:
            #     print("========= ref ==========")
            #     print(ref)
            #     assert ref.isdigit()
            #     return _CONV_REF_SELON_TYPE.get(entites[ref].type)(ref)
            print()
            logger.info(f'elt: {elt}')
            logger.info(f'elt.type : {elt.type}')
            logger.info(f'\n')
            if elt.type == PrimitiveType.POINT:
                return ShaperGeometryGeneration().generateRefToPoint(name)
            elif elt.type == PrimitiveType.LINE:
                return ShaperGeometryGeneration().generateRefToLine(name)
            elif elt.type == PrimitiveType.CIRCLE:
                return ShaperGeometryGeneration().generateRefToCircle(name)
            elif elt.type == PrimitiveType.ARC:
                return ShaperGeometryGeneration().generateRefToArc(name)
            else:
                return None
        else:
            return None

#=================================================================================================================
# generation of constraints :
#=================================================================================================================
    @staticmethod
    def generateHorizontal(elt):
        shaperCode = "# Error in contrainst horizontal("+str(elt.references)+").\n"
        if len(elt.references)==2:
            if elt.references[0].type == PrimitiveType.POINT and elt.references[1].type == PrimitiveType.POINT:
                name = elt.references[0].function_name
                function_name_1 = ShaperGeometryGeneration().generateRefToGeometry(elt.references[0], name)
                name = elt.references[1].function_name
                function_name_2 = ShaperGeometryGeneration().generateRefToGeometry(elt.references[1], name)
                shaperCode = "Sketch_1.setVerticalDistance({}, {}, 0)\n".format(function_name_1, function_name_2)
        elif len(elt.references)==1:
            if elt.references[0].type == PrimitiveType.LINE:
                name = elt.references[0].function_name
                function_name = ShaperGeometryGeneration().generateRefToGeometry(elt.references[0], name)
                shaperCode = "Sketch_1.setHorizontal({})\n".format(function_name)
            else:
                return "# Contrainst horizontal("+str(elt.references[0])+") : this constraint is not implemented.\n"
        return shaperCode

    @staticmethod
    def generateVertical(elt):
        shaperCode = "# Error in contrainst vertical("+str(elt.references)+").\n"
        if len(elt.references)==2:
            if elt.references[0].type == PrimitiveType.POINT and elt.references[1].type == PrimitiveType.POINT:
                name = elt.references[0].function_name
                function_name_1 = ShaperGeometryGeneration().generateRefToGeometry(elt.references[0], name)
                name = elt.references[1].function_name
                function_name_2 = ShaperGeometryGeneration().generateRefToGeometry(elt.references[1], name)
                shaperCode = "Sketch_1.setHorizontalDistance({}, {}, 0)\n".format(function_name_1, function_name_2)
        elif len(elt.references)==1:
            if elt.references[0].type == PrimitiveType.LINE:
                name = elt.references[0].function_name
                function_name = ShaperGeometryGeneration().generateRefToGeometry(elt.references[0], name)
                shaperCode = "Sketch_1.setVertical({})\n".format(function_name)
            else:
                return "# Contrainst vertical("+str(elt.references[0])+") : this constraint is not implemented.\n"
        return shaperCode

    @staticmethod
    def generateParallel(elt):
        shaperCode = "# Error in contrainst parallel("+str(elt.references)+").\n"
        if len(elt.references)==2:
            if elt.references[0].type == PrimitiveType.LINE and elt.references[1].type == PrimitiveType.LINE:
                name = elt.references[0].function_name
                function_name_1 = ShaperGeometryGeneration().generateRefToGeometry(elt.references[0], name)
                name = elt.references[1].function_name
                function_name_2 = ShaperGeometryGeneration().generateRefToGeometry(elt.references[1], name)
                shaperCode = "Sketch_1.setParallel({}, {})\n".format(function_name_1, function_name_2)
        return shaperCode

    @staticmethod
    def generateCoincident(elt):
        logger.info(f'\n\ngenerateCoincident()...............')
        shaperCode = "# Error in contrainst coincident("+str(elt.references)+").\n"
        if len(elt.references)==2:
            ref0 = elt.references[0]
            logger.info(f'ref0 = {ref0}\n')
            logger.info(f'ref0.type, get_name(), get_type() = {ref0.type}, {ref0.get_name}')
            # , {ref0.get_type()}\n')
            name = elt.references[0].function_name
            function_name_1 = ShaperGeometryGeneration().generateRefToGeometry(elt.references[0], name)
            name = elt.references[1].function_name
            function_name_2 = ShaperGeometryGeneration().generateRefToGeometry(elt.references[1], name)
            shaperCode = "Sketch_1.setCoincident({}, {})\n".format(function_name_1, function_name_2)
        return shaperCode


#============================================================================================================
class ShaperConversion(Sketch):

    def export(self, out_path: str):
        """export vers le format python Shaper"""
        with open(out_path, 'wt') as f:
            f.write(ShaperGeometryGeneration.headCode())
            for i,elt in enumerate(self.sequence):
                print()
                print("i, elt =", i+1, elt)
                f.write(ShaperGeometryGeneration.export(i+1,elt))
            f.write(ShaperGeometryGeneration.tailCode())
        f.close()

    def import_file(pythonShaperFile: str) -> Sketch:
    #     """Read a python Shaper file and convert it to sequences of the Skeztch class"""
        pass;    
