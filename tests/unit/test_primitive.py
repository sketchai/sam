import unittest
import logging


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

from sketch_data.factory import create_cad_object

class TestPrimitive(unittest.TestCase):


    def test_Line(self):
        
        # construction 
        line = create_cad_object(label='Line', status_construction = False)

        self.assertFalse(line.is_construction())

        # line.update_parms(parms = {'status_construction' : True})
        # self.assertTrue(line.is_construction())

        
