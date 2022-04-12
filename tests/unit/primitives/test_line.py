from sketch_data.catalog_primitive.line import Line
import unittest
import logging


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


class TestPrimitive(unittest.TestCase):

    def test_construction(self):

        # construction
        line = Line(status_construction=False, pnt1_X=0.2, pnt1_Y=0.2, pnt2_X=0.3, pnt2_Y=0.7)
        self.assertEqual('Line p1=Point P(0.2, 0.2), p2=Point P(0.3, 0.7)', str(line))
        logger.debug(f'line: {line}')
