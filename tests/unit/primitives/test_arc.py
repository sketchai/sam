from sketch_data.catalog_primitive.arc import Arc
import unittest
import logging


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


class TestCircle(unittest.TestCase):

    def test_construction(self):

        # construction
        arc = Arc(status_construction=False, center=[0., 5.], radius=1, angles=[90., 180.])
        self.assertEqual('Arc Center(0.0, 5.0),  radius= 1, start angle= 90.0, end angle= 180.0', str(arc))
        logger.debug(f'arc: {arc}')
