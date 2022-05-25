from typing import List, Dict
from sam.primitive import Primitive, PrimitiveType
from .point import Point

from matplotlib import patches


class Circle(Primitive):
    """Line Primitive."""

    def __init__(self, status_construction: bool = False, center: List = [], radius: float = 0.):
        super(Circle, self).__init__(elt_type=PrimitiveType.CIRCLE, status_construction=status_construction)
        self.center: Point = Point(point = center, status_construction=status_construction)
        self.radius: float = radius

        # add lineage
        self.center.add_parent(self)

    def __repr__(self):
        return f"Circle: center={self.center}, radius=  {self.radius}"

    def _update_radius(self, radius: float):
        self.radius = radius
    
    def _update_center(self, center: List):
        self.center.update_parms({'x' : center[0], 'y': center[1]})

    def _construct_mapp(self) -> None:
        """Construct a mapp to update parameters"""
        return  {'center' : lambda center: self._update_center(center),  
                 'radius' :  lambda radius: self._update_radius(radius)}


    def point_belongs_to_primitive(self, point: object) -> bool:
        """Check if a point belongs to the line"""


    def plot(self, ax, color='black', linewidth=1):
        patch = patches.Circle(self.center.get_point(), self.radius, fill=False, linestyle=self._get_linestyle(), color=color, linewidth=linewidth)
        ax.add_patch(patch)
