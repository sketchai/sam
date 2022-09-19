from sam.catalog_constraint.dimension_constraint import * #Distance, Radius
from sam.catalog_constraint.geometric_constraint import *
from sam.catalog_primitive import Point, Line, Arc, Circle
from sam.catalog_constraint import *
import unittest
import logging

logger = logging.getLogger(__name__)

class TestConstraintGlobal(unittest.TestCase):

    #==================================================================================
    # Contraintes purement géométriques, non dimensionnelles :
    #==================================================================================
    def test_horizontal(self):

        # construction
        line = Line(pnt1= [0.2,0.2], pnt2 = [0.3, 0.7])
        horizontal = Horizontal(references=[line])
        expected_output = 'HORIZONTAL: ref_1: Line p1=Point P(0.2, 0.2), p2=Point P(0.3, 0.7)'
        self.assertEqual(expected_output, str(horizontal))
        logger.debug(f'constraint: {horizontal}')

    def test_vertical(self):

        # construction
        line = Line(pnt1= [0.2,0.2], pnt2 = [0.3, 0.7])
        vertical = Vertical(references=[line])
        expected_output = 'VERTICAL: ref_1: Line p1=Point P(0.2, 0.2), p2=Point P(0.3, 0.7)'
        self.assertEqual(expected_output, str(vertical))
        logger.debug(f'constraint: {vertical}')

    def test_parallel(self):

        # construction
        line_1 = Line(pnt1= [0.2,0.2], pnt2 = [0.3, 0.7])
        line_2 = Line(pnt1= [0.0,0.2], pnt2 = [0.3, 0.7])
        parallel = Parallel(references=[line_1, line_2])
        expected_output = 'PARALLEL: ref_1: Line p1=Point P(0.2, 0.2), p2=Point P(0.3, 0.7), ref_2: Line p1=Point P(0.0, 0.2), p2=Point P(0.3, 0.7)'
        self.assertEqual(expected_output, str(parallel))
        logger.debug(f'constraint: {parallel}')

    def test_coincident(self):

        # construction
        line_1 = Line(pnt1= [0.2,0.2], pnt2 = [0.3, 0.7])
        line_2 = Line(pnt1= [0.0,0.2], pnt2 = [0.3, 0.7])
        coincident = Coincident(references=[line_1.pnt1, line_2.pnt2])
        expected_output = 'COINCIDENT: ref_1: Point P(0.2, 0.2), Line p1=Point P(0.2, 0.2), p2=Point P(0.3, 0.7)-- COINCIDENT: ref_2: Point P(0.3, 0.7), Line p1=Point P(0.0, 0.2), p2=Point P(0.3, 0.7)'
        self.assertEqual(expected_output, str(coincident))
        logger.debug(f'constraint: {coincident}')

    def test_equal(self):

        # same lengths for 2 lines :
        line_1 = Line(pnt1= [0.2,0.2], pnt2 = [0.3, 0.7])
        line_2 = Line(pnt1= [0.0,0.2], pnt2 = [0.1, 0.5])
        constraint = Equal(references=[line_1, line_2])
        expected_output = 'EQUAL: ref_1: Line p1=Point P(0.2, 0.2), p2=Point P(0.3, 0.7), ref_2: Line p1=Point P(0.0, 0.2), p2=Point P(0.1, 0.5)'
        self.assertEqual(expected_output, str(constraint))
        logger.debug(f'constraint: {constraint}')

        # same radius for a circle and an arc of circle ::
        circle = Circle(status_construction=False, center=[0., 5.], radius=1)
        arc = Arc(status_construction=False, center=[0., 5.], radius=1, angles=[90., 180.])
        constraint = Equal(references=[circle, arc])
        expected_output = 'EQUAL: ref_1: Circle: center=Point P(0.0, 5.0), radius=  1, ref_2: Arc center=Point P(0.0, 5.0),  radius= 1, start angle= 90.0, end angle= 180.0'
        self.assertEqual(expected_output, str(constraint))
        logger.debug(f'constraint: {constraint}')

    def test_midpoint(self):

        # construction
        line = Line(pnt1= [0.2,0.2], pnt2 = [0.3, 0.7])
        point = Point(status_construction=False, point=[0., 8.])
        constraint = Midpoint(references=[line, point])
        expected_output = 'MIDPOINT: ref_1: Line p1=Point P(0.2, 0.2), p2=Point P(0.3, 0.7), ref_2: Point P(0.0, 8.0)'
        self.assertEqual(expected_output, str(constraint))
        logger.debug(f'constraint: {constraint}')

    def test_perpendicular(self):

        # construction
        line_1 = Line(pnt1= [0.2,0.2], pnt2 = [0.3, 0.7])
        line_2 = Line(pnt1= [0.0,0.2], pnt2 = [0.3, 0.7])
        constraint = Perpendicular(references=[line_1, line_2])
        expected_output = 'PERPENDICULAR: ref_1: Line p1=Point P(0.2, 0.2), p2=Point P(0.3, 0.7), ref_2: Line p1=Point P(0.0, 0.2), p2=Point P(0.3, 0.7)'
        self.assertEqual(expected_output, str(constraint))
        logger.debug(f'constraint: {constraint}')

    def test_tangent(self):

        # tangence line-circle :
        line = Line(pnt1= [0.2,0.2], pnt2 = [0.3, 0.7])
        circle = Circle(status_construction=False, center=[0., 5.], radius=1)
        constraint = Tangent(references=[line, circle])
        expected_output = 'TANGENT: ref_1: Line p1=Point P(0.2, 0.2), p2=Point P(0.3, 0.7), ref_2: Circle: center=Point P(0.0, 5.0), radius=  1'
        self.assertEqual(expected_output, str(constraint))
        logger.debug(f'constraint: {constraint}')

        # tangence line-arc :
        line = Line(pnt1= [0.2,0.2], pnt2 = [0.3, 0.7])
        arc = Arc(status_construction=False, center=[0., 5.], radius=1, angles=[90., 180.])
        constraint = Tangent(references=[line, arc])
        expected_output = 'TANGENT: ref_1: Line p1=Point P(0.2, 0.2), p2=Point P(0.3, 0.7), ref_2: Arc center=Point P(0.0, 5.0),  radius= 1, start angle= 90.0, end angle= 180.0'
        self.assertEqual(expected_output, str(constraint))
        logger.debug(f'constraint: {constraint}')

    #==================================================================================
    # Contraintes dimensionnelles :
    #==================================================================================
    def test_angle(self):

        # angle constraint between 2 lines :
        line_1 = Line(pnt1= [0.2,0.2], pnt2 = [0.3, 0.7])
        line_2 = Line(pnt1= [0.0,0.2], pnt2 = [0.3, 0.7])
        constraint = Angle(references=[line_1, line_2], angle = 45.)
        expected_output = 'ANGLE: ref_1: Line p1=Point P(0.2, 0.2), p2=Point P(0.3, 0.7), ref_2: Line p1=Point P(0.0, 0.2), p2=Point P(0.3, 0.7), angle = 45.0'
        self.assertEqual(expected_output, str(constraint))
        logger.debug(f'constraint: {constraint}')

    def test_length(self):

        # construction
        line = Line(pnt1= [0.2,0.2], pnt2 = [0.3, 0.7])
        length = Length(references=[line], length=2.)
        expected_output = 'LENGTH: ref= Line p1=Point P(0.2, 0.2), p2=Point P(0.3, 0.7), length = 2.0'
        self.assertEqual(expected_output, str(length))
        logger.debug(f'constraint: {length}')

    def test_distance(self):

        # distance entre 2 segments (line) :
        line_1 = Line(pnt1= [0.2,0.2], pnt2 = [0.3, 0.7])
        line_2 = Line(pnt1= [0.0,0.2], pnt2 = [0.3, 0.7])
        constraint = Distance(references=[line_1, line_2], distance_min=5)
        expected_output = 'DISTANCE: ref_1: Line p1=Point P(0.2, 0.2), p2=Point P(0.3, 0.7), ref_2: Line p1=Point P(0.0, 0.2), p2=Point P(0.3, 0.7), distance_min = 5'
        self.assertEqual(expected_output, str(constraint))
        logger.debug(f'constraint: {constraint}')

        # distance entre un segment (line) et un point :
        line = Line(pnt1= [0.1,0.2], pnt2 = [0.3, 0.7])
        point = Point(status_construction=False, point=[0., 8.])
        constraint = Distance(references=[line, point], distance_min=5)
        expected_output = 'DISTANCE: ref_1: Line p1=Point P(0.1, 0.2), p2=Point P(0.3, 0.7), ref_2: Point P(0.0, 8.0), distance_min = 5'
        self.assertEqual(expected_output, str(constraint))
        logger.debug(f'constraint: {constraint}')

    def test_horizontaldistance(self):

        # distance entre 2 segments (line) :
        line_1 = Line(pnt1= [0.2,0.2], pnt2 = [0.3, 0.7])
        line_2 = Line(pnt1= [0.0,0.2], pnt2 = [0.3, 0.7])
        constraint = HorizontalDistance(references=[line_1, line_2], distance_min=5)
        expected_output = 'HORIZONTAL_DISTANCE: ref_1: Line p1=Point P(0.2, 0.2), p2=Point P(0.3, 0.7), ref_2: Line p1=Point P(0.0, 0.2), p2=Point P(0.3, 0.7), distance_min = 5'
        self.assertEqual(expected_output, str(constraint))
        logger.debug(f'constraint: {constraint}')

        # distance entre un segment (line) et un point :
        line = Line(pnt1= [0.1,0.2], pnt2 = [0.3, 0.7])
        point = Point(status_construction=False, point=[0., 8.])
        constraint = HorizontalDistance(references=[line, point], distance_min=5)
        expected_output = 'HORIZONTAL_DISTANCE: ref_1: Line p1=Point P(0.1, 0.2), p2=Point P(0.3, 0.7), ref_2: Point P(0.0, 8.0), distance_min = 5'
        self.assertEqual(expected_output, str(constraint))
        logger.debug(f'constraint: {constraint}')

        # distance with a single line:
        line = Line(pnt1= [0.1,0.2], pnt2 = [0.3, 0.7])
        constraint = HorizontalDistance(references=[line], distance_min=5)
        expected_output = 'HORIZONTAL_DISTANCE: ref_1: Line p1=Point P(0.1, 0.2), p2=Point P(0.3, 0.7), distance_min = 5'
        self.assertEqual(expected_output, str(constraint))
        logger.debug(f'constraint: {constraint}')

    def test_verticaldistance(self):

        # distance entre 2 segments (line) :
        line_1 = Line(pnt1= [0.2,0.2], pnt2 = [0.3, 0.7])
        line_2 = Line(pnt1= [0.0,0.2], pnt2 = [0.3, 0.7])
        constraint = VerticalDistance(references=[line_1, line_2], distance_min=5)
        expected_output = 'VERTICAL_DISTANCE: ref_1: Line p1=Point P(0.2, 0.2), p2=Point P(0.3, 0.7), ref_2: Line p1=Point P(0.0, 0.2), p2=Point P(0.3, 0.7), distance_min = 5'
        self.assertEqual(expected_output, str(constraint))
        logger.debug(f'constraint: {constraint}')

        # distance entre un segment (line) et un point :
        line = Line(pnt1= [0.1,0.2], pnt2 = [0.3, 0.7])
        point = Point(status_construction=False, point=[0., 8.])
        constraint = VerticalDistance(references=[line, point], distance_min=5)
        expected_output = 'VERTICAL_DISTANCE: ref_1: Line p1=Point P(0.1, 0.2), p2=Point P(0.3, 0.7), ref_2: Point P(0.0, 8.0), distance_min = 5'
        self.assertEqual(expected_output, str(constraint))
        logger.debug(f'constraint: {constraint}')

        # distance with a single line:
        line = Line(pnt1= [0.1,0.2], pnt2 = [0.3, 0.7])
        constraint = VerticalDistance(references=[line], distance_min=5)
        expected_output = 'VERTICAL_DISTANCE: ref_1: Line p1=Point P(0.1, 0.2), p2=Point P(0.3, 0.7), distance_min = 5'
        self.assertEqual(expected_output, str(constraint))
        logger.debug(f'constraint: {constraint}')

    def test_radius(self):

        # test de contrainte rayon sur un cercle :
        circle = Circle(status_construction=False, center=[0., 5.], radius=1)
        constraint = Radius(references=[circle], radius=2.)
        expected_output = 'RADIUS: ref= Circle: center=Point P(0.0, 5.0), radius=  1, radius = 2.0'
        self.assertEqual(expected_output, str(constraint))
        logger.debug(f'constraint: {constraint}')

        # test de contrainte rayon sur un arc de cercle :
        arc = Arc(status_construction=False, center=[0., 5.], radius=1, angles=[90., 180.])
        constraint = Radius(references=[arc], radius=2.)
        expected_output = 'RADIUS: ref= Arc center=Point P(0.0, 5.0),  radius= 1, start angle= 90.0, end angle= 180.0, radius = 2.0'
        self.assertEqual(expected_output, str(constraint))
        logger.debug(f'constraint: {constraint}')


