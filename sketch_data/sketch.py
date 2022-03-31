from typing import List
import pickle, sys
import matplotlib.pyplot as plt

from sketch_data.primitive import Primitive
from sketch_data.constraint import Constraint

sys.path.append("/home/H03832/Donnees/GAN_CAO/gitlab_pleiade/SketchGraphs_For_EDF/sketchgraphs")
from sketchgraphs.data import flat_array
import sketchgraphs.data as datalib

class Sketch:
    def __init__(self):
        self.sequence: List[Int] = []

    def add(self, elt: object):
        self.sequence.append(elt)

    def _prepare_draw(self, ax=None, show_axes: bool = True):
        if ax is None:
            fig = plt.figure()
            ax = fig.add_subplot(111, aspect='equal')
        else:
            fig = None

        # Eliminate upper and right axes
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')

        if not show_axes:
            ax.set_yticklabels([])
            ax.set_xticklabels([])
            _ = [line.set_marker('None') for line in ax.get_xticklines()]
            _ = [line.set_marker('None') for line in ax.get_yticklines()]

            # Eliminate lower and left axes
            ax.spines['left'].set_color('none')
            ax.spines['bottom'].set_color('none')

        return fig, ax

    def draw(self, show_axes: bool = True):

        fig, ax = self._prepare_draw()
        for s in self.sequence:
            if isinstance(s, Primitive):
                p_fn = s.plot(ax)
                if p_fn is None:
                    continue

        # Rescale axis limits
        ax.relim()
        ax.autoscale_view()

        return fig

    def read_random_sequence_from_Sketchgraphs_file(self, dataset = 'sg_t16_validation.npy'):
        # 'sg_t16_train.npy'
        import sys, random, logging
        logging.basicConfig(level=logging.DEBUG)
        logger = logging.getLogger()

        data_path = "/home/H03832/Donnees/GAN_CAO/gitlab/data_sous_Marc/"
        seq_data = flat_array.load_dictionary_flat(data_path+dataset)
        print("*********************************************************************")
        print(len(seq_data['sequences']), "séquences")
        i = random.randint(0,len(seq_data['sequences']))
        print("index séquence :", i)
        seq = seq_data['sequences'][i]
        print("Longueur de la séquence =", len(seq))
        cpt = 0
        for _, s in enumerate(seq):
            if 'NodeOp' in str(s):
                # print(f'index= {cpt}, s={s}')
                logger.info(f'index= {cpt}, s={s}')
                cpt += 1
            else :
                # print(f'........... s= {s}')
                logger.info(f'........... s= {s}')
        # sketch = datalib.sketch_from_sequence(seq)
        # datalib.render_sketch(sketch, show_axes=True, show_origin=True);

    def export(self, out_path: str):
        pickle.dump({'seq': self.sequence}, open(out_path, "wb"))
