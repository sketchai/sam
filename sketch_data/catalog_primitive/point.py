from typing import List, Dict
from sketch_data.primitive import Primitive, PrimitiveType


class Point(Primitive):
    """Point Primitive."""

    def __init__(self, status_construction: bool = False, point: List = [], threshold: float = 0.00001):
        super(Point, self).__init__(elt_type=PrimitiveType.POINT, status_construction=status_construction)
        self.x: float = point[0]
        self.y: float = point[1]
        self.threshold: float = threshold

    def __repr__(self):
        return f"Point P({self.x}, {self.y})"

    def point_belongs_to_primitive(self, point: List) -> bool:
        """Check if a point belongs to the point"""
        return np.linalg.norm(np.array([self.x, self.y]), point) < self.threshold

    def update_parms(self, parms: Dict) -> object:
        """Update the current parameters"""
        pass

        # for new_p, parms in zip(l_parms, l_new_parms):
        #     if
        #     self.is_construction = parms.get('construction', None)

    def plot(self, ax, color='black'):
        ax.scatter(self.x, self.y, c=color, marker='.')
