from sam.catalog_primitive import Circle, Line, Arc
from sam.sketch import Sketch
import unittest
import logging
import matplotlib.pyplot as plt
import pickle
from pathlib import Path


logger = logging.getLogger(__name__)


class TestSketch(unittest.TestCase):

    def test_init(self):

        # construction
        sketch = Sketch()

        sketch.add(Circle(center=[10., 5.], radius=1))
        sketch.add(Line(pnt1 = [0.2, 0.2], pnt2 = [0.3, 0.7]))

        for s in sketch.sequence:
            logger.info(f'{s}')

    # def test_show(self):
    #     sketch = Sketch()

    #     sketch.add(Circle(center=[0.,5.], radius=1))
    #     sketch.add(Arc(center=[0.,5.], radius=1, angles = [90.,180.]))
    #     sketch.add(Line(pnt1 = [0.2, 0.2], pnt2 = [0.3, 0.7]))

    #     fig = sketch.draw()
    #     plt.show()

    def test_export(self):
        sketch = Sketch()
        sketch.add(Circle(center=[0., 5.], radius=1))
        
        filename = Path('tests/asset/out/')
        filename.mkdir(parents=True, exist_ok=True)

        out_path = 'tests/asset/out/sketch.pkl'
        sketch.export(out_path=out_path)

        seq = pickle.load(open(out_path, "rb"))
        logger.info(f'seq: {seq}')
