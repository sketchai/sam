from typing import Dict, List
from sketch_data.constraint import Constraint, ConstraintType


class Length(Constraint):
    """Line Primitive."""

    def __init__(self, status_construction: bool = False, references: List = [], length: float = None):
        super(Length, self).__init__(c_type=ConstraintType.LENGTH, status_construction=status_construction, references=references)
        self.length = length

    def __repr__(self):
        elt = self.references[0]
        return f"Horizontal: ref= {elt}, length = {self.length}"

    def update_parms(self, parms: Dict) -> object:
        pass
