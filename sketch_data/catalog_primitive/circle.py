from typing import List, Dict
from sketch_data.primitive import Primitive, PrimitiveType

from matplotlib import patches


class Circle(Primitive):
    """Line Primitive."""

    def __init__(self, status_construction: bool = False, center: List = [], radius: float = 0.):
        super(Circle, self).__init__(elt_type=PrimitiveType.CIRCLE, status_construction=status_construction)
        self.x_center: float = center[0]
        self.y_center: float = center[1]
        self.radius: float = radius

    def __repr__(self):
        return f"Circle: Center O({self.x_center}, {self.y_center}), radius=  {self.radius}"

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
        patch = patches.Circle((self.x_center, self.y_center), self.radius, fill=False, linestyle=self._get_linestyle(), color=color)
        ax.add_patch(patch)
