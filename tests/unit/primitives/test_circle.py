from sam.catalog_primitive.circle import Circle
import unittest
import logging


logger = logging.getLogger(__name__)


class TestCircle(unittest.TestCase):

    def test_construction(self):

        # construction
        circle = Circle(status_construction=False, center=[0., 5.], radius=1)
        self.assertEqual('Circle: center=Point P(0.0, 5.0), radius=  1', str(circle))
        logger.debug(f'circle: {circle}')

    def test_update_parms(self):
        circle = Circle(status_construction=False, center=[0., 5.], radius=1)
        self.assertEqual('Circle: center=Point P(0.0, 5.0), radius=  1', str(circle))
        circle.update_parms({'center' : [1., 7.], 'radius' : 0.8}) 
        self.assertEqual('Circle: center=Point P(1.0, 7.0), radius=  0.8', str(circle)) 

    def test_lineage(self):

        # Test 1: test that the three objects have the same references
        circle = Circle(status_construction=False, center=[0., 5.], radius=1)
        self.assertTrue(circle is circle.center.parent)

        # Test 2: test that when line is modify, parents are modify
        circle.update_parms({'center' : [1., 7.], 'radius' : 0.8}) 
        self.assertEqual('Circle: center=Point P(1.0, 7.0), radius=  0.8', str(circle)) 
        self.assertEqual('Circle: center=Point P(1.0, 7.0), radius=  0.8', str(circle.center.parent))   
