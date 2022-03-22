from typing import Dict 
from sketch_data.primitive import Primitive, PrimitiveType

class Line(Primitive):
    """Line Primitive."""

    def __init__(self, status_construction:bool =False, pnt1_X: float =0, pnt1_Y: float =0, pnt2_X: float=1, pnt2_Y: float=0):
        super(Line, self).__init__(status_construction)
        self.pnt1_X: float = pnt1_X
        self.pnt1_Y: float = pnt1_Y
        self.pnt2_X: float = pnt2_X
        self.pnt2_Y: float = pnt2_Y

    @property
    def type(self):
        return PrimitiveType.Line

    def from_feat(self, feat, is_construction : bool = False):
        p1 = feat.firstPoint()
        p2 = feat.lastPoint()
        return Line(is_construction=is_construction, pnt1_X=p1.x(), pnt1_Y=p1.y(), pnt2_X=p2.x(), pnt2_Y=p2.y())


    def __repr__(self):
        return f"Line p1({self.pnt1_X}, {self.pnt1_Y}) p2({self.pnt2_X}, {self.pnt2_Y})"  

    
    def point_belongs_to_primitive(self, point:object) -> bool:
        """Construct from a shaper object"""

    def update_parms(self, parms:Dict) -> object:
        """Update the current parameters"""