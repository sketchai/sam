import enum
import abc
from typing import Dict

import logging


logger = logging.getLogger(__name__)


class PrimitiveType(enum.IntEnum):
    """This enumeration represents the type of the geometries."""
    LINE = 0
    ARC = 1
    CIRCLE = 2
    POINT = 3


class Primitive(abc.ABC):
    """Abstract class representing a geometry entity.

    This abstract class represents a geometric entity in a sketch.
    It is identified by its entity id, a unique string within the sketch.
    """

    def __init__(self, elt_type: object, status_construction: bool = False):
        self.status_construction: bool = status_construction
        self.type: int = elt_type

    def _get_linestyle(self):
        return '--' if self.status_construction else '-'

    def is_construction(self) -> bool:
        return self.status_construction

    @property
    def get_name(self) -> int:
        return self.type.name

    @property
    def get_type(self) -> int:
        return self.type


    def _construct_mapp(self) -> object:
        """Construct a mapp to update parameters"""
        pass

    def point_belongs_to_primitive(self, point: object) -> object:
        """Construct from a shaper object"""
        pass

    def update_parms(self, parms: Dict) -> None:
        """Update the current parameters"""
        mapp = self._construct_mapp()

        
        for key, elt in parms.items():
            mapp[key](elt)

    # @abc.abstractmethod
    # def to_dict(self) -> dict:
    #     """Obtains a serialized representation of this entity as a dictionary.

    #     The returned dictionary should be compatible with the json representation from onshape.
    #     """
