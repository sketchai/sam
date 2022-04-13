from sketch_data.catalog_primitive.circle import Circle
import unittest
import logging


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


class TestCircle(unittest.TestCase):

    def test_construction(self):

        # construction
        circle = Circle(status_construction=False, center=[0., 5.], radius=1)
        self.assertEqual('Circle: center=Point P(0.0, 5.0), radius=  1', str(circle))
        logger.debug(f'circle: {circle}')
