from typing import List, Dict
from sketch_data.primitive import PrimitiveType
from .point import Point
from .circle import Circle

from matplotlib import patches

import logging


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


class Arc(Circle):
    """Arc Primitive."""

    def __init__(self, status_construction: bool = False, center: List = [], radius: float = 0., angles: List = []):
        super().__init__(status_construction=status_construction, center = center, radius = radius)
        self.type = PrimitiveType.ARC
        
        self.angle_start: float = angles[0]  # in degrees
        self.angle_end: float = angles[1]  # in degrees

    def __repr__(self):
        return f"Arc center={self.center},  radius= {self.radius}, start angle= {self.angle_start}, end angle= {self.angle_end}"

    def _update_angle_start(self,angle: float):
        self.angle_start = angle
    
    def _update_angle_end(self, angle: float):
        self.angle_end = angle

    def _construct_mapp(self) -> None:
        """Construct a mapp to update parameters"""
        mapp = super()._construct_mapp()
        mapp['angle_start'] = lambda angle : self._update_angle_start(angle)
        mapp['angle_end'] = lambda angle : self._update_angle_end(angle)
        return  mapp

    def point_belongs_to_primitive(self, point: object) -> bool:
        """Check if a point belongs to the line"""

    def plot(self, ax, color='black', linewidth=1):
        #angle = math.atan2(arc.yDir, arc.xDir) * 180 / math.pi
        #startParam = arc.startParam * 180 / math.pi
        #endParam = arc.endParam * 180 / math.pi

        ax.add_patch(patches.Arc(xy=self.center.get_point(),  # center of the ellipse
                                 # angle=self.angle_start - self.angle_end, # rotation of the ellipse, counterclockwise, in degrees
                                 theta1=self.angle_start,  # starting angle, in degrees
                                 theta2=self.angle_end,  # ending angle, in degrees
                                 width=2 * self.radius,  # The length of the horizontal axis.
                                 height=2 * self.radius,  # The length of the vertical axis.
                                 linestyle=self._get_linestyle(), color=color))
