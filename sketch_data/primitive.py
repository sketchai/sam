import enum
import abc
from typing import Dict

class PrimitiveType(enum.IntEnum):
    """This enumeration represents the type of the geometries."""
    Line = 0


class Primitive(abc.ABC):
    """Abstract class representing a geometry entity.

    This abstract class represents a geometric entity in a sketch.
    It is identified by its entity id, a unique string within the sketch.
    """

    def __init__(self, status_construction: bool = False):
        self.status_construction: bool = status_construction

    def is_construction(self):
        return self.status_construction

    @property
    @abc.abstractmethod
    def type(self) -> object:
        """Get the concrete type of the underlying entity."""

    @abc.abstractmethod
    def update_parms(self, parms:Dict) -> object:
        """Update the current parameters"""

    @abc.abstractmethod
    def from_feat(self, feat:object) -> object:
        """Construct from a shaper object"""

    @abc.abstractmethod
    def point_belongs_to_primitive(self, point:object) -> object:
        """Construct from a shaper object"""

    # @abc.abstractmethod
    # def to_dict(self) -> dict:
    #     """Obtains a serialized representation of this entity as a dictionary.

    #     The returned dictionary should be compatible with the json representation from onshape.
    #     """



