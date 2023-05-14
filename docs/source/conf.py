from datetime import date

import os
import sys
from pathlib import Path

from packaging.version import Version

HERE = Path(__file__).parent
LITE = HERE.parent / "lite"
ROOT = HERE.parent.parent
JLW = ROOT / "python/jupyterlab_widgets"
IPYW = ROOT / "python/ipywidgets"
WIDG = ROOT / "python/widgetsnbextension"
TYPD = HERE.parent / "typedoc"
NODM = ROOT / "node_modules"
TSBI = [
    p.parent / "tsconfig.tsbuildinfo" for p in ROOT.glob("packages/*/tsconfig.json")
]

# work around unpickleable functions
sys.path.append(str(HERE))
from ipywidgets_docs_utils import jupyterlab_markdown_heading, run_if_needed

# silence debug messages
os.environ["PYDEVD_DISABLE_FILE_VALIDATION"] = "1"

def on_config_inited(*args):
    """rebuild"""

    run_if_needed(["jlpm"], ROOT, [NODM])
    run_if_needed(["jlpm", "build"], ROOT, TSBI)
    run_if_needed(["jlpm", "docs"], ROOT, [TYPD / "typedoc/index.html"])

    for pkg_root in [IPYW, WIDG, JLW]:
        run_if_needed(["pyproject-build"], pkg_root, [pkg_root / "dist"])

    run_if_needed(["jupyter", "lite", "build"], LITE)

def setup(app):
    app.connect("config-inited", on_config_inited)


# -- Sphinx extensions and configuration ------------------------

extensions = [
    'myst_nb',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx_autodoc_typehints',
    'sphinx_copybutton',
    'sphinx.ext.viewcode',
    'sphinxext.rediraffe',
    'IPython.sphinxext.ipython_console_highlighting',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'ipython': ('https://ipython.readthedocs.io/en/stable/', None),
    'nbconvert': ('https://nbconvert.readthedocs.io/en/stable', None),
    'nbformat': ('https://nbformat.readthedocs.io/en/stable', None),
    'traitlets': ('https://traitlets.readthedocs.io/en/stable', None),
}

# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'ElectroLab'

author = 'J.G.Aguado'
email = 'jon-garcia@hotmail.com'

release = '3'
version = '1'

today = date.today()
compile_date = today.strftime("%B %d, %Y")

# -- Project information

rst_epilog  = """
.. |Product| replace:: %s
.. |Author| replace:: %s
.. |Email| replace:: %s
.. |Release| replace:: %s
.. |Date| replace:: %s
""" % (project, author, email, release, compile_date)


# -- General configuration

# extensions = [
#     'sphinx.ext.duration',
#     'sphinx.ext.doctest',
#     'sphinx.ext.autodoc',
#     'sphinx.ext.autosummary',
#     'sphinx.ext.intersphinx',
#     'sphinx_copybutton',
# ]
# intersphinx_mapping = {
#     'python': ('https://docs.python.org/3/', None),
#     'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
# }
# intersphinx_disabled_domains = ['std']

# templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'logo_only': True,
    'navigation_depth': 5,
}
html_context = {}

html_logo = "images/logo/White.png"
html_show_sourcelink = True
html_static_path = ['_static']

# -- Options for EPUB output
epub_show_urls = 'footnote'
