from typing import Dict, List
from sketch_data.constraint import Constraint, ConstraintType


class Diameter(Constraint):

    def __init__(self, status_construction: bool = False, references: List = [], radius: float = None):
        super(Length, self).__init__(elt_type=ConstraintType.DIAMETER, status_construction=status_construction, references=references)
        self.diameter = diameter

    def __repr__(self):
        elt = self.references[0]
        return f"{self.get_name()}: ref= {elt}, diameter = {self.diameter}"


class Length(Constraint):

    def __init__(self, status_construction: bool = False, references: List = [], length: float = None):
        super(Length, self).__init__(elt_type=ConstraintType.LENGTH, status_construction=status_construction, references=references)
        self.length = length

    def __repr__(self):
        elt = self.references[0]
        return f"{self.get_name()}: ref= {elt}, length = {self.length}"

class Radius(Constraint):

    def __init__(self, status_construction: bool = False, references: List = [], radius: float = None):
        super(Radius, self).__init__(elt_type=ConstraintType.RADIUS, status_construction=status_construction, references=references)
        self.radius = radius

    def __repr__(self):
        elt = self.references[0]
        return f"{self.get_name()}: ref= {elt}, radius = {self.radius}"
