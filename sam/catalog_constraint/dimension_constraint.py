from typing import Dict, List
from sam.constraint import Constraint, ConstraintType

class Angle(Constraint):

    def __init__(self, references: List = [], angle: float = None):
        super(Angle, self).__init__(elt_type=ConstraintType.ANGLE, references=references)
        self.angle = angle

    def __repr__(self):
        elt1 = self.references[0]
        elt2 = self.references[1]
        return f"{self.get_name()}: ref_1: {elt1}, ref_2: {elt2}, angle = {self.angle}"

    def _update_angle(self, angle: float):
        self.angle = angle

    def _construct_mapp(self) -> Dict:
        """Construct a mapp to update parameters"""
        mapp = {'angle' : lambda angle : self._update_angle(angle)}
        return  mapp

class Distance(Constraint):

    def __init__(self, references: List = [], distance_min: float = None):
        super(Distance, self).__init__(elt_type=ConstraintType.DISTANCE, references=references)
        self.distance_min = distance_min

    def __repr__(self):
        elt1 = self.references[0]
        if len(self.references) == 2 :
            elt2 = self.references[1]
            return f"{self.get_name()}: ref_1: {elt1}, ref_2: {elt2}, distance_min = {self.distance_min}"
        else :
            return f"{self.get_name()}: ref_1: {elt1}, distance_min = {self.distance_min}"

    def _update_distance_min(self, distance_min: float):
        self.distance_min = distance_min

    def _construct_mapp(self) -> Dict:
        """Construct a mapp to update parameters"""
        mapp = {'distance_min' : lambda x : self._update_distance_min(x)}
        return  mapp

class HorizontalDistance(Distance):

    def __init__(self, references: List = [], distance_min: float = None):
        super(Distance, self).__init__(elt_type=ConstraintType.DISTANCE, references=references)
        self.type = ConstraintType.HORIZONTAL_DISTANCE
        self.distance_min = distance_min


class VerticalDistance(Distance):

    def __init__(self, references: List = [], distance_min: float = None):
        super(Distance, self).__init__(elt_type=ConstraintType.DISTANCE, references=references)
        self.type = ConstraintType.VERTICAL_DISTANCE
        self.distance_min = distance_min


class Length(Constraint):

    def __init__(self, references: List = [], length: float = None):
        super(Length, self).__init__(elt_type=ConstraintType.LENGTH, references=references)
        self.length = length

    def __repr__(self):
        elt = self.references[0]
        return f"{self.get_name()}: ref= {elt}, length = {self.length}"

    def _update_length(self, length: float):
        self.length = length

    def _construct_mapp(self) -> Dict:
        """Construct a mapp to update parameters"""
        mapp = {'length' : lambda x : self._update_length(x)}
        return  mapp




class Radius(Constraint):

    def __init__(self, references: List = [], radius: float = None):
        super(Radius, self).__init__(elt_type=ConstraintType.RADIUS, references=references)
        self.radius = radius

    def __repr__(self):
        elt = self.references[0]
        return f"{self.get_name()}: ref= {elt}, radius = {self.radius}"

    def _update_radius(self, radius: float):
        self.radius = radius

    def _construct_mapp(self) -> Dict:
        """Construct a mapp to update parameters"""
        mapp = {'radius' : lambda x : self._update_radius(x)}
        return  mapp