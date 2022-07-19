from typing import Dict, List
from sam.primitive import Primitive, PrimitiveType
from .point import Point

import logging
logger = logging.getLogger(__name__)

class Line(Primitive):
    """Line Primitive."""

    def __init__(self, status_construction: bool = False, pnt1: List = [], pnt2: List = []):
        super(Line, self).__init__(elt_type=PrimitiveType.LINE, status_construction=status_construction)
        self.pnt1: Point=Point(point=pnt1)
        self.pnt2: Point=Point(point=pnt2)

        # add lineage
        self.pnt1.add_parent(self)
        self.pnt2.add_parent(self)

    def __repr__(self):
        return f"Line p1={self.pnt1}, p2={self.pnt2}"

    def point_belongs_to_primitive(self, point: object) -> bool:
        """Check if a point belongs to the line"""

    def _construct_mapp(self) -> None:
        """Construct a mapp to update parameters"""
        return  {   'pnt1' : lambda x: self.pnt1.update_parms({'x' : x[0], 'y': x[1]}), 
                    'pnt2' : lambda x: self.pnt2.update_parms({'x' : x[0], 'y': x[1]})}


    def plot(self, ax, color='black', linewidth=1):
        ax.scatter(self.pnt1.x, self.pnt1.y, c='red', marker='.')
        ax.scatter(self.pnt2.x, self.pnt2.y, c='blue', marker='.')
        ax.plot([self.pnt1.x, self.pnt2.x], [self.pnt1.y, self.pnt2.y], color, linestyle=self._get_linestyle(), linewidth=linewidth)
