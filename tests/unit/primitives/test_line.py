from sam.catalog_primitive.line import Line
import unittest
import logging


logger = logging.getLogger(__name__)


class TestPrimitive(unittest.TestCase):

    def test_construction(self):

        # construction
        line = Line(status_construction=False, pnt1 = [0.2,0.2], pnt2= [0.3, 0.7])
        self.assertEqual('Line p1=Point P(0.2, 0.2), p2=Point P(0.3, 0.7)', str(line))
        logger.debug(f'line: {line}')

    def test_update_parms(self):
        line = Line(status_construction=False, pnt1 = [0.2,0.2], pnt2= [0.3, 0.7])
        self.assertEqual('Line p1=Point P(0.2, 0.2), p2=Point P(0.3, 0.7)', str(line))
        line.update_parms({'pnt1' : [0.3, 0.4], 'pnt2' : [0.1,0.8]}) 
        self.assertEqual('Line p1=Point P(0.3, 0.4), p2=Point P(0.1, 0.8)', str(line)) 


    def test_lineage(self):

        # Test 1: test that the three objects have the same references
        line = Line(status_construction=False, pnt1 = [0.2,0.2], pnt2= [0.3, 0.7])
        self.assertTrue(line is line.pnt1.parent)
        self.assertTrue(line is line.pnt2.parent)
        self.assertTrue(line.pnt1.parent is line.pnt2.parent)
        logger.debug(f'parent: {line.pnt1.parent}')
        logger.debug(f'line: {line}')

        # Test 2: test that when line is modify, parents are modify
        line.update_parms({'pnt1' : [0.3, 0.4], 'pnt2' : [0.1,0.8]}) 
        self.assertEqual('Line p1=Point P(0.3, 0.4), p2=Point P(0.1, 0.8)', str(line))
        self.assertEqual('Line p1=Point P(0.3, 0.4), p2=Point P(0.1, 0.8)', str(line.pnt1.parent))  
        self.assertEqual('Line p1=Point P(0.3, 0.4), p2=Point P(0.1, 0.8)', str(line.pnt2.parent))  
