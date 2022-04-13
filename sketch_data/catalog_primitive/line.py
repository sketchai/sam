from typing import Dict, List
from sketch_data.primitive import Primitive, PrimitiveType
from .point import Point

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
        return  {   'pnt1_X' : lambda x: self.pnt1._update_x(x),  'pnt1_Y' :  lambda y: self.pnt1._update_y(y),
                    'pnt2_X' : lambda x: self.pnt2._update_x(x), 'pnt2_Y': lambda y: self.pnt2._update_y(y)}


    def plot(self, ax, color='black', linewidth=1):
        ax.plot(self.pnt1.get_point(), self.pnt2.get_point(), color, linestyle=self._get_linestyle(), linewidth=linewidth)
