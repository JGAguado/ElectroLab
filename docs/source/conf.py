from datetime import date

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

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'logo_only': True,
    'navigation_depth': 5,
    'collapse_navigation' : False,

}
html_context = {}

html_logo = "images/logo/White.png"
html_show_sourcelink = True
html_static_path = ['_static']

# -- Options for EPUB output
epub_show_urls = 'footnote'

def setup(app):
    app.add_css_file('my_theme.css')