from _primitive import Primitive

class Circle(Entity):
    """Circle Entity."""

    xCenter: float
    yCenter: float
    xDir: float
    yDir: float
    radius: float
    clockwise: bool

    float_ids = ['xCenter', 'yCenter', 'xDir', 'yDir', 'radius']
    bool_ids = Entity.bool_ids + ['clockwise']

    def __init__(self, entityId, isConstruction=False, xCenter=0, yCenter=0, xDir=1, yDir=0, radius=1, clockwise=False):
        super(Circle, self).__init__(entityId, isConstruction)
        self.xCenter = xCenter
        self.yCenter = yCenter
        self.xDir = xDir
        self.yDir = yDir
        self.radius = radius
        self.clockwise = clockwise

    @property
    def type(self):
        return EntityType.Circle

    def get_subnode_ids(self):
        return (self.entityId + '.center',)

    @staticmethod
    def get_subnode_types():
        return (SubnodeType.SN_Center,)

    def to_dict(self):
        return {
            'message': {
                'entityId': self.entityId,
                'centerId': self.entityId + '.center',
                'isConstruction': self.isConstruction,
                'geometry': {
                    'message': {
                        'xCenter': self.xCenter,
                        'yCenter': self.yCenter,
                        'xDir': self.xDir,
                        'yDir': self.yDir,
                        'radius': self.radius,
                        'clockwise': self.clockwise
                    },
                    'type': 115,
                    'typeName': 'BTCurveGeometryCircle',
                },
            },
            'type': 4,
            'typeName': 'BTMSketchCurve',
        }

    @property
    def center_point(self):
        return np.array([self.xCenter, self.yCenter])

    @staticmethod
    def from_dict(ent_dict):
        msg_dict = ent_dict['message']
        geom_dict = msg_dict['geometry']['message']

        return Circle(
            *_get_entity_common_attributes(ent_dict),
            float(geom_dict['xCenter']),
            float(geom_dict['yCenter']),
            float(geom_dict['xDir']),
            float(geom_dict['yDir']),
            float(geom_dict['radius']),
            bool(geom_dict['clockwise']))

    @staticmethod
    def from_info(ent_info):
        xCenter, yCenter = ent_info['center']
        xDir, yDir = 1.0, 0.0
        radius = ent_info['radius']
        clockwise = bool(ent_info.get('clockwise', False))

        return Circle(ent_info['id'],
                      bool(ent_info.get('isConstruction', False)),
                      xCenter, yCenter, xDir, yDir,
                      radius, clockwise)

    def __repr__(self):
        return (f"Circle [{self.entityId}] c({self.xCenter}, {self.yCenter}) " +
                f"d({self.xDir}, {self.yDir}) r({self.radius}) " +
                f"{'clockwise' if self.clockwise else 'anti-clockwise'}")

