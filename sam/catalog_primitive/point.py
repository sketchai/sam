from typing import List, Dict
from sam.primitive import Primitive, PrimitiveType


class Point(Primitive):
    """Point Primitive."""

    def __init__(self, status_construction: bool = False, point: List = []):
        super(Point, self).__init__(elt_type=PrimitiveType.POINT, status_construction=status_construction)
        self.x: float = point[0]
        self.y: float = point[1]

    def __repr__(self):
        return f"Point P({self.x}, {self.y})"

    def _update_x(self,x : float):
        self.x = x 

    def _update_y(self,y : float):
        self.y = y 

    def _construct_mapp(self) -> None:
        """Construct a mapp to update parameters"""
        return  {'x' :  lambda x: self._update_x(x),  'y' : lambda y:self._update_y(y)}

    def add_parent(self,parent:object) -> None:
        self.parent = parent

    def get_point(self):
        return [self.x , self.y ]

    def point_belongs_to_primitive(self, point: List, threshold: float = 0.00001) -> bool:
        """Check if a point belongs to the point"""
        return np.linalg.norm(np.array([self.x, self.y]), point) < self.threshold



    def plot(self, ax, color='black',**kwargs):
        ax.scatter(self.x, self.y, color=color, marker='.',**kwargs)
