import sys
from pathlib import Path

sys.path.append(str(Path('_ext').resolve()))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'hackerspace.edu.pl'
copyright = '2025, hackerspace.edu.pl project'
author = 'hackerspace.edu.pl project'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
   "sphinx_copybutton",
   "sphinx_external_toc",
   "rst2pdf.pdfbuilder",
       # Sphinx's own extensions
    # "sphinx.ext.autodoc",
    # "sphinx.ext.extlinks",
    # "sphinx.ext.intersphinx",
    # "sphinx.ext.mathjax",
    # "sphinx.ext.todo",
    # "sphinx.ext.viewcode",
    # Our custom extension, only meant for Furo's own documentation.
    # "furo.sphinxext",
    # External stuff
    # "myst_parser",
    # "sphinx_design",
    # "sphinx_inline_tabs",
    "noop" # used to ignore specific directives to make the HTML manual
]

external_toc_exclude_missing = False  # optional, default: False
external_toc_path = "_toc.yaml" # "toc" for Table of Contents, this is the navigation
templates_path = ['_templates']
exclude_patterns = ['examples/*']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# source_suffix = { ".md": "markdown" }
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}
html_title = "hackerspace.edu.pl"
html_theme = 'furo'
html_logo = 'assets/logo.png'
html_favicon = 'assets/favicon.ico'

# -- Options for PDF output --------------------------------------------------

pdf_documents = [('manual', u'hackerspace.edu.pl', u'hackerspace.edu.pl documentation', u'hackerspace.edu.pl project'),]
