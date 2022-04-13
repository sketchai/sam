from sketch_data.catalog_primitive import Point, Line, Circle, Arc
from sketch_data.catalog_constraint import *
from sketch_data.shaper_sketch import ShaperConversion
from sketch_data.sketch import Sketch
import unittest
import logging
import matplotlib.pyplot as plt
import pickle

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


class TestShaperSketch(unittest.TestCase):

    def test_init(self):

        # construction
        sketch = ShaperConversion()
        # sketch.add(Circle(center=[0., 5.], radius=1))
        sketch.add(Point(point=(2,6)))
        l1 = Line(pnt1_X=0.2, pnt1_Y=0.2, pnt2_X=0.3, pnt2_Y=0.7)
        sketch.add(l1)
        sketch.add(Horizontal([l1]))

    def test_read_random_sequence_from_Sketchgraphs_file(self):
        sketch = ShaperConversion()
        sketch.read_random_sequence_from_Sketchgraphs_file()

    # def test_show(self):
    #     sketch = Sketch()

    #     sketch.add(Circle(center=[0.,5.], radius=1))
    #     sketch.add(Arc(center=[0.,5.], radius=1, angles = [90.,180.]))
    #     sketch.add(Line(pnt1_X =0.2, pnt1_Y = 0.2, pnt2_X = 0.3, pnt2_Y=0.7))

    #     fig = sketch.draw()
    #     plt.show()

    def test_export_1(self):
        sketch = ShaperConversion()
        l1 = Line(status_construction=True, pnt1_X=1, pnt1_Y=2, pnt2_X=3, pnt2_Y=4)
        sketch.add(l1)
        l2 = Line(status_construction=False, pnt1_X=-1, pnt1_Y=-2, pnt2_X=-3, pnt2_Y=-4)
        sketch.add(l2)
        sketch.add(Parallel([l1, l2]))
        sketch.add(Horizontal([l2]))

        out_path = 'tests/unit/asset/out/export_shaper_sketch_1.py'
        sketch.export(out_path=out_path)

        seq = sketch.sequence
        logger.info(f'seq: {seq}')

    def test_export_2(self):
        sketch = ShaperConversion()
        p1 = Point(point=(2,6))
        sketch.add(p1)
        c1 = Circle(center=[3.,5.], radius=3)
        sketch.add(c1)
        a1 = Arc(status_construction=True, center=[0.,0.], radius=1, angles = [270.,180.])
        sketch.add(a1)
        sketch.add(Coincident([c1,a1]))

        out_path = 'tests/unit/asset/out/export_shaper_sketch_2.py'
        sketch.export(out_path=out_path)

        seq = sketch.sequence
        logger.info(f'seq: {seq}')
