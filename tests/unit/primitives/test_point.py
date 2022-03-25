from sketch_data.catalog_primitive.point import Point
import unittest
import logging


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


class TestCircle(unittest.TestCase):

    def test_construction(self):

        # construction
        point = Point(status_construction=False, point=[0., 1.])
        self.assertEqual('Point P(0.0, 1.0)', str(point))
        logger.debug(f'point: {point}')
