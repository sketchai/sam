from sam.catalog_primitive.point import Point
import unittest
import logging


logger = logging.getLogger(__name__)


class TestCircle(unittest.TestCase):

    def test_construction(self):

        # construction
        point = Point(status_construction=False, point=[0., 1.])
        self.assertEqual('Point P(0.0, 1.0)', str(point))
        logger.debug(f'point: {point}')

    def test_update_parms(self):
        point = Point(status_construction=False, point=[0., 1.])
        self.assertEqual('Point P(0.0, 1.0)', str(point))
        point.update_parms({'x' : 0.3, 'y' : 0.4}) 
        self.assertEqual('Point P(0.3, 0.4)', str(point)) 