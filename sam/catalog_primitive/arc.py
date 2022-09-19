from typing import List, Dict
from sam.primitive import Primitive, PrimitiveType
from .point import Point

from matplotlib import patches
import numpy as np

import logging


logger = logging.getLogger(__name__)


class Arc(Primitive):
    """Arc Primitive."""

    def __init__(self, status_construction: bool = False, center: List = [], radius: float = 0., angles: List = [], radian=False):
        super().__init__(elt_type=PrimitiveType.ARC, status_construction=status_construction)
        self.center: Point = Point(point = center, status_construction=status_construction)
        self.radius: float = radius
        self.angle_start: float = angles[0]  
        self.angle_end: float = angles[1]  
        self.radian: bool = radian 

        # add lineage
        self.center.add_parent(self)

    def __repr__(self):
        return f"Arc center={self.center},  radius= {self.radius}, start angle= {self.angle_start}, end angle= {self.angle_end}"

    def add_points_startend(self):
        if not self.radian:
            angle_start = np.deg2rad(self.angle_start)
            angle_end = np.deg2rad(self.angle_end)
        else:
            angle_start = self.angle_start
            angle_end = self.angle_end
        self.pnt1 = Point(point = [self.center.x + self.radius*np.cos(angle_start), self.center.y + self.radius*np.sin(angle_start)]) 
        self.pnt2 = Point(point = [self.center.x + self.radius*np.cos(angle_end), self.center.y + self.radius*np.sin(angle_end)]) 

        # add lineage
        self.pnt1.add_parent(self)
        self.pnt2.add_parent(self)
        
    def _update_angle_start(self,angle: float):
        self.angle_start = angle
    
    def _update_angle_end(self, angle: float):
        self.angle_end = angle

    def _update_radius(self, radius: float):
        self.radius = radius
    
    def _update_center(self, center: List):
        self.center.update_parms({'x' : center[0], 'y': center[1]})

    def _construct_mapp(self) -> None:
        """Construct a mapp to update parameters"""

    def _construct_mapp(self) -> None:
        """Construct a mapp to update parameters"""
        mapp = {
            'center': lambda center: self._update_center(center),  
            'radius':  lambda radius: self._update_radius(radius),
            'angle_start': lambda angle : self._update_angle_start(angle),
            'angle_end': lambda angle : self._update_angle_end(angle),}
        if hasattr(self,'pnt1'):
            mapp['pnt1'] = lambda x: self.pnt1.update_parms({'x' : x[0], 'y': x[1]})
            mapp['pnt2'] = lambda x: self.pnt2.update_parms({'x' : x[0], 'y': x[1]})
        return  mapp

    def point_belongs_to_primitive(self, point: object) -> bool:
        """Check if a point belongs to the line"""

    def plot(self, ax, color='black', linewidth=1):
        #angle = math.atan2(arc.yDir, arc.xDir) * 180 / math.pi
        #startParam = arc.startParam * 180 / math.pi
        #endParam = arc.endParam * 180 / math.pi
        theta1 = self.angle_start
        theta2 = self.angle_end
        if self.radian:
            theta1 = np.rad2deg(theta1)
            theta2 = np.rad2deg(theta2)
        ax.add_patch(patches.Arc(xy=self.center.get_point(),  # center of the ellipse
                                 # angle=self.angle_start - self.angle_end, # rotation of the ellipse, counterclockwise, in degrees
                                 theta1=theta1,  # starting angle, in degrees
                                 theta2=theta2,  # ending angle, in degrees
                                 width=2 * self.radius,  # The length of the horizontal axis.
                                 height=2 * self.radius,  # The length of the vertical axis.
                                 linewidth=linewidth,
                                 linestyle=self._get_linestyle(), color=color))
