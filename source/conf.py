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
   "noop" # used to ignore specific directives to make the HTML manual
]

external_toc_path = "_toc.yaml" # "toc" for Table of Contents, this is the navigation
templates_path = ['_templates']
exclude_patterns = ['examples/*']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_logo = 'assets/logo.png'
html_favicon = 'assets/favicon.ico'
html_theme_options = {
    "sidebar_hide_name": True,
    "navigation_with_keys": True,
    "top_of_page_buttons": ["view", "edit"],
    "source_repository": "https://github.com/hackerspace-edu-pl/hackerspace.edu.pl.github.io",
    "source_branch": "main",
    "source_directory": "source/",
}

# -- Options for PDF output --------------------------------------------------

pdf_documents = [('manual', u'hackerspace', u'hackerspace documentation', u'hackerspace project'),]
