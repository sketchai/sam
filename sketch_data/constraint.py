import enum
import abc
from typing import Dict, List


class ConstraintType(enum.IntEnum):
    """This enumeration represents the type of the constraints."""
    HORIZONTAL = 0
    PARALLEL = 1
    LENGTH = 2
    COINCIDENT = 3
    PERPENDICULAR = 4
    DIAMETER = 5
    DISTANCE = 6
    RADIUS = 7



    # PROJECTED = 1
    # MIRROR = 2
    # 

    # VERTICAL = 6
    # TANGENT = 7

    # 
    # MIDPOINT = 10
    # EQUAL = 11
    # 
    # OFFSET = 13

    # CONCENTRIC = 15
    # FIX = 16
    # ANGLE = 17
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

    def __init__(self, elt_type: str, status_construction: bool = False, references: List = []):
        self.status_construction: bool = status_construction
        self.type: str = elt_type
        self.references: str = references

    def is_construction(self):
        return self.status_construction


    def get_name(self) -> int:
        return self.type.name


    def get_type(self) -> int:
        return self.type

    # @abc.abstractmethod
    def update_parms(self, parms: Dict) -> object:
        """Update the current parameters"""
        pass

    def __repr__(self):
        l_ref = [f'ref_{i+1}: {ref}' for i, ref in enumerate(self.references)]
        refs = ', '.join(l_ref)
        return f"{self.get_name()}: {refs}"