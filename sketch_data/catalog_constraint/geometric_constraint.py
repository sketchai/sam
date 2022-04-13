from typing import Dict, List
from sketch_data.constraint import Constraint, ConstraintType

class Coincident(Constraint):

    def __init__(self, references: List = []):
        super(Coincident, self).__init__(elt_type=ConstraintType.COINCIDENT, references=references)

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
