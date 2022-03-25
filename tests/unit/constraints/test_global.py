from sketch_data.catalog_primitive import Line
from sketch_data.catalog_constraint import *
import unittest
import logging


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


class TestConstraintGlobal(unittest.TestCase):

    def test_horizontal(self):

        # construction
        line = Line(pnt1_X=0.2, pnt1_Y=0.2, pnt2_X=0.3, pnt2_Y=0.7)
        horizontal = Horizontal(references=[line])
        self.assertEqual('HORIZONTAL: ref_1: Line p1(0.2, 0.2) p2(0.3, 0.7)', str(horizontal))
        logger.debug(f'constraint: {horizontal}')

    def test_length(self):

        # construction
        line = Line(pnt1_X=0.2, pnt1_Y=0.2, pnt2_X=0.3, pnt2_Y=0.7)
        length = Length(references=[line], length=2.)
        self.assertEqual('LENGTH: ref= Line p1(0.2, 0.2) p2(0.3, 0.7), length = 2.0', str(length))
        logger.debug(f'constraint: {length}')

    def test_parallel(self):

        # construction
        line_1 = Line(pnt1_X=0.2, pnt1_Y=0.2, pnt2_X=0.3, pnt2_Y=0.7)
        line_2 = Line(pnt1_X=0.0, pnt1_Y=0.2, pnt2_X=0.3, pnt2_Y=0.7)
        parallel = Parallel(references=[line_1, line_2])
        self.assertEqual('PARALLEL: ref_1: Line p1(0.2, 0.2) p2(0.3, 0.7), ref_2: Line p1(0.0, 0.2) p2(0.3, 0.7)', str(parallel))
        logger.debug(f'constraint: {parallel}')

    def test_coincident(self):

        # construction
        line_1 = Line(pnt1_X=0.2, pnt1_Y=0.2, pnt2_X=0.3, pnt2_Y=0.7)
        line_2 = Line(pnt1_X=0.0, pnt1_Y=0.2, pnt2_X=0.3, pnt2_Y=0.7)
        constraint = Coincident(references=[line_1, line_2])
        self.assertEqual('COINCIDENT: ref_1: Line p1(0.2, 0.2) p2(0.3, 0.7), ref_2: Line p1(0.0, 0.2) p2(0.3, 0.7)', str(constraint))
        logger.debug(f'constraint: {constraint}')

    def test_perpendicular(self):

        # construction
        line_1 = Line(pnt1_X=0.2, pnt1_Y=0.2, pnt2_X=0.3, pnt2_Y=0.7)
        line_2 = Line(pnt1_X=0.0, pnt1_Y=0.2, pnt2_X=0.3, pnt2_Y=0.7)
        constraint = Perpendicular(references=[line_1, line_2])
        self.assertEqual('PERPENDICULAR: ref_1: Line p1(0.2, 0.2) p2(0.3, 0.7), ref_2: Line p1(0.0, 0.2) p2(0.3, 0.7)', str(constraint))
        logger.debug(f'constraint: {constraint}')