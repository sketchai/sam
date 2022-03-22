from _primitive import Primitive


class Point(Entity):
    """Point Entity."""

    float_ids = ['x', 'y']
    bool_ids = Entity.bool_ids

    def __init__(self, entityId, isConstruction=False, x=0, y=0):
        super(Point, self).__init__(entityId, isConstruction)
        self.x = x
        self.y = y

    @property
    def type(self):
        return EntityType.Point

    def to_dict(self):
        return {
            'type': 158,
            'typeName': 'BTMSketchPoint',
            'message': {
                'entityId': self.entityId,
                'isConstruction': self.isConstruction,
                'x': self.x,
                'y': self.y
            }
        }

    def __iter__(self):
        return iter((self.x, self.y))

    def __getitem__(self, idx):
        if idx == 0:
            return self.x
        elif idx == 1:
            return self.y
        else:
            raise IndexError()

    @staticmethod
    def from_dict(ent_dict):
        if ent_dict['typeName'] != 'BTMSketchPoint':
            raise ValueError('invalid dictionary for entity type Point')

        msg_dict = ent_dict['message']
        return Point(*_get_entity_common_attributes(ent_dict),
                     float(msg_dict['x']), float(msg_dict['y']))

    @staticmethod
    def from_info(ent_info):
        return Point(ent_info['id'],
                     bool(ent_info.get('isConstruction', False)),
                     float(ent_info['point'][0]),
                     float(ent_info['point'][1]))

    def __repr__(self):
        return f"Point [{self.entityId}] ({self.x, self.y})"