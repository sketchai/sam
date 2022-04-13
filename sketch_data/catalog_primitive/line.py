from typing import Dict
from sketch_data.primitive import Primitive, PrimitiveType
from .point import Point

class Line(Primitive):
    """Line Primitive."""

    def __init__(self, status_construction: bool = False, pnt1_X: float = 0, pnt1_Y: float = 0, pnt2_X: float = 1, pnt2_Y: float = 0):
        super(Line, self).__init__(elt_type=PrimitiveType.LINE, status_construction=status_construction)
        self.pnt1: Point=Point(point=[pnt1_X, pnt1_Y])
        self.pnt2: Point=Point(point=[pnt2_X, pnt2_Y])

    def __repr__(self):
        return f"Line p1={self.pnt1}, p2={self.pnt2}"

    def point_belongs_to_primitive(self, point: object) -> bool:
        """Check if a point belongs to the line"""

    def update_parms(self, parms: Dict) -> object:
        """Update the current parameters"""
        l_parms = [self.is_construction, self.pnt1_X, self.pnt1_Y, self.pnt2_X, self.pnt2_Y]
        l_new_parms = ['construction', 'pnt1_X', 'pnt1_Y', 'pnt2_X', 'pnt2_Y']
        pass

        # for new_p, parms in zip(l_parms, l_new_parms):
        #     if
        #     self.is_construction = parms.get('construction', None)

    def plot(self, ax, color='black', linewidth=1):
        ax.plot(self.pnt1.get_point(), self.pnt2.get_point(), color, linestyle=self._get_linestyle(), linewidth=linewidth)
