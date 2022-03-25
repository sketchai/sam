from typing import Dict, List
from sketch_data.constraint import Constraint, ConstraintType


class Horizontal(Constraint):
    """Line Primitive."""

    def __init__(self, status_construction: bool = False, references: List = []):
        super(Horizontal, self).__init__(c_type=ConstraintType.HORIZONTAL, status_construction=status_construction, references=references)

    def __repr__(self):
        elt = self.references[0]
        return f"Horizontal: ref= {elt}"

    def update_parms(self, parms: Dict) -> object:
        pass
