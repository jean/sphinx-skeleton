""" Generate index entries for everything
"""

import sys
import random
from monkey import wrap
from docutils.parsers.rst.directives import images
from docutils.parsers.rst.directives.images import Figure
from sphinx import addnodes

@wrap(Figure.run, '93931c51f5f01322672f5d080eef6853a0a28e3e')
def run(original_run, self):
    figure_nodes = original_run(self)
    self.indexnode = addnodes.index(entries=[])
    name = random.randint(0, 10000)
    targetname = 'figure.' + str(name)
    indextext = 'testing'
    self.indexnode['entries'].append(('single', indextext, targetname, ''))
    figure_nodes.append(self.indexnode)
    return figure_nodes

Figure.run = run

def setup(app):
    """Sphinx extension setup function.

    When the extension is loaded, Sphinx imports this module and executes
    the ``setup()`` function, which in turn notifies Sphinx of everything
    the extension offers.
    """
    from sphinx.application import Sphinx
    if not isinstance(app, Sphinx):
        return  # probably called by tests

