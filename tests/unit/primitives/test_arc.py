from sam.catalog_primitive.arc import Arc
import unittest
import logging


logger = logging.getLogger(__name__)


class TestArc(unittest.TestCase):

    def test_construction(self):

        # construction
        arc = Arc(status_construction=False, center=[0., 5.], radius=1, angles=[90., 180.])
        self.assertEqual('Arc center=Point P(0.0, 5.0),  radius= 1, start angle= 90.0, end angle= 180.0', str(arc))
        logger.debug(f'arc: {arc}')

    def test_update_parms(self):
        arc = Arc(status_construction=False, center=[0., 5.], radius=1, angles=[90., 180.])
        self.assertEqual('Arc center=Point P(0.0, 5.0),  radius= 1, start angle= 90.0, end angle= 180.0', str(arc))
        arc.update_parms({'center' : [1., 7.], 'radius' : 0.8, 'angle_start': 50.0, 'angle_end': 66.0}) 
        self.assertEqual('Arc center=Point P(1.0, 7.0),  radius= 0.8, start angle= 50.0, end angle= 66.0', str(arc)) 

    def test_lineage(self):

        # Test 1: test that the three objects have the same references
        arc = Arc(status_construction=False, center=[0., 5.], radius=1, angles=[90., 180.])
        self.assertTrue(arc is arc.center.parent)

        # Test 2: test that when line is modify, parents are modify
        arc.update_parms({'center' : [1., 7.], 'radius' : 0.8, 'angle_start': 50.0, 'angle_end': 66.0}) 
        self.assertEqual('Arc center=Point P(1.0, 7.0),  radius= 0.8, start angle= 50.0, end angle= 66.0', str(arc)) 
        self.assertEqual('Arc center=Point P(1.0, 7.0),  radius= 0.8, start angle= 50.0, end angle= 66.0', str(arc.center.parent))  
