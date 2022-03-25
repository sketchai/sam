import enum
import abc
from typing import Dict, List


class ConstraintType(enum.IntEnum):
    """This enumeration represents the type of the geometries."""
    HORIZONTAL = 0
    LENGTH = 1
    PARALLEL = 2


class Constraint(abc.ABC):
    """Abstract class representing a geometry entity.

    This abstract class represents a geometric entity in a sketch.
    It is identified by its entity id, a unique string within the sketch.
    """

    def __init__(self, c_type: str, status_construction: bool = False, references: List = []):
        self.status_construction: bool = status_construction
        self.name: str = c_type.name
        self.elt_type: str = c_type
        self.references: str = references

    def is_construction(self):
        return self.status_construction

    @property
    def type(self):
        return self.type

    @abc.abstractmethod
    def update_parms(self, parms: Dict) -> object:
        """Update the current parameters"""
