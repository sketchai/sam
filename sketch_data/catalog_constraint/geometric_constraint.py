from typing import Dict, List
from sketch_data.constraint import Constraint, ConstraintType

class Coincident(Constraint):

    def __init__(self, status_construction: bool = False, references: List = []):
        super(Coincident, self).__init__(elt_type=ConstraintType.COINCIDENT, status_construction=status_construction, references=references)


class Horizontal(Constraint):
    """Horizontal constraint"""

    def __init__(self, status_construction: bool = False, references: List = []):
        super(Horizontal, self).__init__(elt_type=ConstraintType.HORIZONTAL, status_construction=status_construction, references=references)



class Parallel(Constraint):
    """Parallel Constraint"""

    def __init__(self, status_construction: bool = False, references: List = []):
        super(Parallel, self).__init__(elt_type=ConstraintType.PARALLEL, status_construction=status_construction, references=references)

class Perpendicular(Constraint):
    """Parallel Constraint"""

    def __init__(self, status_construction: bool = False, references: List = []):
        super(Perpendicular, self).__init__(elt_type=ConstraintType.PERPENDICULAR, status_construction=status_construction, references=references)
