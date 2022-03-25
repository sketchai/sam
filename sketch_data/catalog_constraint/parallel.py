from typing import Dict, List
from sketch_data.constraint import Constraint, ConstraintType


class Parallel(Constraint):
    """Parallel Constraint"""

    def __init__(self, status_construction: bool = False, references: List = []):
        super(Parallel, self).__init__(c_type=ConstraintType.PARALLEL, status_construction=status_construction, references=references)

    def update_parms(self, parms: Dict) -> object:
        pass

    def __repr__(self):
        elt_1 = self.references[0]
        elt_2 = self.references[0]
        return f"Parallel: ref_1 = {elt_1}, ref_2 = {elt_2}"
