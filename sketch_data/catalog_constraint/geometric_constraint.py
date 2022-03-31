from typing import Dict, List
from sketch_data.constraint import Constraint, ConstraintType

class Coincident(Constraint):

    def __init__(self, references: List = []):
        super(Coincident, self).__init__(elt_type=ConstraintType.COINCIDENT, references=references)


class Horizontal(Constraint):
    """Horizontal constraint"""

    def __init__(self, references: List = []):
        super(Horizontal, self).__init__(elt_type=ConstraintType.HORIZONTAL, references=references)



class Parallel(Constraint):
    """Parallel Constraint"""

    def __init__(self, references: List = []):
        super(Parallel, self).__init__(elt_type=ConstraintType.PARALLEL, references=references)

class Perpendicular(Constraint):
    """Parallel Constraint"""

    def __init__(self, references: List = []):
        super(Perpendicular, self).__init__(elt_type=ConstraintType.PERPENDICULAR, references=references)
