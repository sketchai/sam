from sketch_data.catalog_primitive import Circle, Line, Arc
from sketch_data.sketch import Sketch
import unittest
import logging
import matplotlib.pyplot as plt
import pickle

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


class TestSketch(unittest.TestCase):

    def test_init(self):

        # construction
        sketch = Sketch()

        sketch.add(Circle(center=[0., 5.], radius=1))
        sketch.add(Line(pnt1_X=0.2, pnt1_Y=0.2, pnt2_X=0.3, pnt2_Y=0.7))

    def test_show(self):
        sketch = Sketch()

        sketch.add(Circle(center=[0.,5.], radius=1))
        sketch.add(Arc(center=[0.,5.], radius=1, angles = [90.,180.]))
        sketch.add(Line(pnt1_X =0.2, pnt1_Y = 0.2, pnt2_X = 0.3, pnt2_Y=0.7))

        fig = sketch.draw()
        plt.show()

    def test_export(self):
        sketch = Sketch()
        sketch.add(Circle(center=[0., 5.], radius=1))

        out_path = 'tests/unit/asset/out/sketch.pkl'
        sketch.export(out_path=out_path)

        seq = pickle.load(open(out_path, "rb"))
        logger.info(f'seq: {seq}')
