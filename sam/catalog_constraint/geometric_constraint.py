from typing import Dict, List
from sam.constraint import Constraint, ConstraintType

class Coincident(Constraint):

    def __init__(self, references: List = []):
        super(Coincident, self).__init__(elt_type=ConstraintType.COINCIDENT, references=references)

    def __repr__(self):
        elt1 = self.references[0]
        elt2 = self.references[1]
        if hasattr(elt1, 'parent'):
            rep = f"{self.get_name()}: ref_1: {elt1}, {elt1.parent}"
        else :
            rep = f"{self.get_name()}: ref_1: {elt1}"
        if hasattr(elt2, 'parent'):
            rep += f"-- {self.get_name()}: ref_2: {elt2}, {elt2.parent}"
        else :
            rep += f"-- {self.get_name()}: ref_2: {elt2}"

        return rep

class Equal(Constraint):
    """Equal Constraint (same length for lines or same radius for circles or arcs"""

    def __init__(self, references: List = []):
        super(Equal, self).__init__(elt_type=ConstraintType.EQUAL, references=references)

class Horizontal(Constraint):
    """Horizontal constraint"""

    def __init__(self, references: List = []):
        super(Horizontal, self).__init__(elt_type=ConstraintType.HORIZONTAL, references=references)

class Midpoint(Constraint):

    def __init__(self, references: List = []):
        super(Midpoint, self).__init__(elt_type=ConstraintType.MIDPOINT, references=references)

class Vertical(Constraint):
    """Vertical constraint"""

    def __init__(self, references: List = []):
        super(Vertical, self).__init__(elt_type=ConstraintType.VERTICAL, references=references)

class Tangent(Constraint):
    """Tangent Constraint"""

    def __init__(self, references: List = []):
        super(Tangent, self).__init__(elt_type=ConstraintType.TANGENT, references=references)

class Parallel(Constraint):
    """Parallel Constraint"""

    def __init__(self, references: List = []):
        super(Parallel, self).__init__(elt_type=ConstraintType.PARALLEL, references=references)

class Perpendicular(Constraint):
    """Perpendicular Constraint"""

    def __init__(self, references: List = []):
        super(Perpendicular, self).__init__(elt_type=ConstraintType.PERPENDICULAR, references=references)
