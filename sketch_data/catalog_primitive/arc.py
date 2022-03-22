from _primitive import Primitive

class Arc(Entity):
    """Arc entity"""

    xCenter: float
    yCenter: float
    xDir: float
    yDir: float
    radius: float
    clockwise: bool
    startParam: float
    endParam: float

    float_ids = ['xCenter', 'yCenter', 'xDir', 'yDir', 'radius', 'startParam', 'endParam']
    bool_ids = Circle.bool_ids

    def __init__(self, entityId, isConstruction=False,
                 xCenter=0, yCenter=0, xDir=1, yDir=0,
                 radius=1, clockwise=False, startParam=-0.5, endParam=0.5):
        super(Arc, self).__init__(entityId, isConstruction)
        self.xCenter = xCenter
        self.yCenter = yCenter
        self.xDir = xDir
        self.yDir = yDir
        self.radius = radius
        self.clockwise = clockwise
        self.startParam = startParam
        self.endParam = endParam

    @property
    def type(self):
        return EntityType.Arc

    def get_subnode_ids(self):
        return (self.entityId + '.center', self.entityId + '.start', self.entityId + '.end')

    @staticmethod
    def get_subnode_types():
        return (SubnodeType.SN_Center, SubnodeType.SN_Start, SubnodeType.SN_End)

    def to_dict(self):
        return {
            'message': {
                'centerId': self.entityId + '.center',
                'entityId': self.entityId,
                'isConstruction': self.isConstruction,
                'startParam': self.startParam,
                'endParam': self.endParam,
                'startPointId': self.entityId + '.start',
                'endPointId': self.entityId + '.end',
                'geometry': {
                    'type': 115,
                    'typeName': 'BTCurveGeometryCircle',
                    'message': {
                        'xCenter': self.xCenter,
                        'yCenter': self.yCenter,
                        'xDir': self.xDir,
                        'yDir': self.yDir,
                        'radius': self.radius,
                        'clockwise': self.clockwise
                    }
                }
            },
            'type': 155,
            'typeName': 'BTMSketchCurveSegment',
        }

    @staticmethod
    def from_dict(ent_dict):
        msg_dict = ent_dict['message']
        geom_dict = msg_dict['geometry']['message']

        return Arc(
            *_get_entity_common_attributes(ent_dict),
            float(geom_dict['xCenter']),
            float(geom_dict['yCenter']),
            float(geom_dict['xDir']),
            float(geom_dict['yDir']),
            float(geom_dict['radius']),
            bool(geom_dict['clockwise']),
            float(msg_dict['startParam']),
            float(msg_dict['endParam']))

    @staticmethod
    def from_info(ent_info):
        xCenter, yCenter = ent_info['center']
        xDir, yDir = 1.0, 0.0
        radius = ent_info['radius']
        clockwise = bool(ent_info.get('clockwise', False))
        startVec = np.array(ent_info['startPoint']) - np.array(ent_info['center'])
        endVec = np.array(ent_info['endPoint']) - np.array(ent_info['center'])
        startParam = math.atan2(startVec[1], startVec[0])
        endParam = math.atan2(endVec[1], endVec[0])
        if clockwise:
            # Convert to counterclockwise
            tmp_start = startParam
            startParam = endParam
            endParam = tmp_start

        return Arc(ent_info['id'],
                   bool(ent_info.get('isConstruction', False)),
                   xCenter, yCenter, xDir, yDir,
                   radius, False, startParam, endParam)

    def _point_at_angle_offset(self, angle_offset):
        angle = math.atan2(self.yDir, self.xDir)
        if self.clockwise:
            angle_offset *= -1
        angle_start = angle + angle_offset
        xStart = self.xCenter + (math.cos(angle_start) * self.radius)
        yStart = self.yCenter + (math.sin(angle_start) * self.radius)
        return np.array([xStart, yStart])

    @property
    def start_point(self):
        """Returns tuple representing coordinates of arc start point."""
        return self._point_at_angle_offset(self.startParam)

    @property
    def end_point(self):
        """Returns tuple representing coordinates of arc end point."""
        return self._point_at_angle_offset(self.endParam)

    @property
    def center_point(self):
        return np.array([self.xCenter, self.yCenter])

    def __repr__(self):
        return (f"Arc [{self.entityId}] c({self.xCenter}, {self.yCenter}) " +
                f"d({self.xDir}, {self.yDir}) r({self.radius}) " +
                f"{'clockwise' if self.clockwise else 'anti-clockwise'}")
