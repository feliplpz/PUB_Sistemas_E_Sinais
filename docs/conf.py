"""Sphinx configuration."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

project = 'Sistemas e Sinais'
copyright = '2025, Felipe Lopez'
author = 'Felipe Lopez'
release = '0.1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'numpydoc',
]

templates_path = ['_templates']
exclude_patterns = ['_build']

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

napoleon_numpy_docstring = True
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
}
