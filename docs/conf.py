# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Unum · UDisk'
copyright = '2023, Unum'
author = 'Unum'
release = open('../VERSION', 'r').read().strip()
with open('_static/custom.js', 'r+') as js:
    content = js.read()
    js.seek(0)
    js.truncate()
    js.write(content.replace("$(VERSION)", release))
# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'breathe', 'm2r2',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinxcontrib.jquery',
    'sphinxcontrib.googleanalytics']

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '*.md']


googleanalytics_id = 'UA-150644745-1'
googleanalytics_enabled = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_logo = '../assets/unum.png'
html_theme = 'furo'
html_static_path = ['_static']
html_css_files = [
    'custom.css'
]
html_js_files = [
    'custom.js'
]


breathe_projects = {'UDisk': '../build/xml'}
breathe_default_project = 'UDisk'
