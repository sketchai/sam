from typing import List
import pickle, sys
import matplotlib.pyplot as plt

from sam.primitive import Primitive
from sam.constraint import Constraint

import logging
logger = logging.getLogger(__name__)

class Sketch:
    def __init__(self):
        self.sequence: List = []

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
        ax.grid(True)
        ax.relim()
        ax.autoscale_view()

        return fig

    def export(self, out_path: str):
        logger.info(f'save in {out_path}')
        pickle.dump({'seq': self.sequence}, open(out_path, "wb"))
