from typing import Dict, List
from sketch_data.constraint import Constraint, ConstraintType

class Angle(Constraint):

    def __init__(self, references: List = [], angle: float = None):
        super(Angle, self).__init__(elt_type=ConstraintType.ANGLE, references=references)
        self.angle = angle

    def __repr__(self):
        elt1 = self.references[0]
        elt2 = self.references[1]
        return f"{self.get_name()}: ref_1: {elt1}, ref_2: {elt2}, angle = {self.angle}"

class Distance(Constraint):

    def __init__(self, references: List = [], distance_min: float = None):
        super(Distance, self).__init__(elt_type=ConstraintType.DISTANCE, references=references)
        self.distance_min = distance_min

    def __repr__(self):
        elt1 = self.references[0]
        elt2 = self.references[1]
        return f"{self.get_name()}: ref_1: {elt1}, ref_2: {elt2}, distance_min = {self.distance_min}"

class Length(Constraint):

    def __init__(self, references: List = [], length: float = None):
        super(Length, self).__init__(elt_type=ConstraintType.LENGTH, references=references)
        self.length = length

    def __repr__(self):
        elt = self.references[0]
        return f"{self.get_name()}: ref= {elt}, length = {self.length}"

class HorizontalLength(Constraint):

    def __init__(self, references: List = [], length: float = None):
        super(HorizontalLength, self).__init__(elt_type=ConstraintType.HORIZONTAL_LENGTH, references=references)
        self.length = length

    def __repr__(self):
        elt = self.references[0]
        return f"{self.get_name()}: ref= {elt}, length = {self.length}"

class VerticalLength(Constraint):

    def __init__(self, references: List = [], length: float = None):
        super(VerticalLength, self).__init__(elt_type=ConstraintType.VERTICAL_LENGTH, references=references)
        self.length = length

    def __repr__(self):
        elt = self.references[0]
        return f"{self.get_name()}: ref= {elt}, length = {self.length}"

class Radius(Constraint):

    def __init__(self, references: List = [], radius: float = None):
        super(Radius, self).__init__(elt_type=ConstraintType.RADIUS, references=references)
        self.radius = radius

    def __repr__(self):
        elt = self.references[0]
        return f"{self.get_name()}: ref= {elt}, radius_constraint = {self.radius}"
