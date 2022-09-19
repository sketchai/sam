import enum
import abc
from typing import Dict, List


class ConstraintType(enum.IntEnum):
    """This enumeration represents the type of the constraints."""
    HORIZONTAL = 0
    VERTICAL = 1
    PARALLEL = 2
    LENGTH = 3
    COINCIDENT = 4
    PERPENDICULAR = 5
    DISTANCE = 7
    RADIUS = 8
    TANGENT = 9
    MIDPOINT = 10
    EQUAL = 11
    ANGLE = 12
    HORIZONTAL_DISTANCE = 13
    VERTICAL_DISTANCE = 14
    # PROJECTED = 1
    # MIRROR = 2
    # 

    # 

    # 
    # OFFSET = 13

    # CONCENTRIC = 15
    # FIX = 16

    # CIRCULAR_PATTERN = 18
    # PIERCE = 19
    # LINEAR_PATTERN = 20
    # CENTERLINE_DIMENSION = 21
    # INTERSECTED = 22
    # SILHOUTTED = 23
    # QUADRANT = 24
    # NORMAL = 25
    # MINOR_DIAM = 26
    # MAJOR_DIAM = 27
    # RHO = 28

class Constraint(abc.ABC):
    """Abstract class representing a geometry entity.

    This abstract class represents a geometric entity in a sketch.
    It is identified by its entity id, a unique string within the sketch.
    """

    def __init__(self, elt_type: object, references: List = []):
        self.type: object = elt_type
        self.references: List = references

    def __repr__(self):
        l_ref = [f'ref_{i+1}: {ref}' for i, ref in enumerate(self.references)]
        refs = ', '.join(l_ref)
        return f"{self.get_name()}: {refs}"

    def get_name(self) -> str:
        return self.type.name

    def get_type(self) -> object:
        return self.type

    def _construct_mapp(self) -> object:
        """Construct a mapp to update parameters"""
        pass

    def update_parms(self, parms: Dict) -> None:
        """Update the current parameters"""
        mapp = self._construct_mapp()

        for key, elt in parms.items():
            mapp[key](elt)

