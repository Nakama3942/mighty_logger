# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Mighty Logger'
copyright = ' Copyright 2023 Kalynovsky Valentin. All rights reserved.'
author = 'Kalynovsky Valentin'
release = 'v1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.todo']

templates_path = ['_templates']
exclude_patterns = []

language = 'en'
master_doc = 'index'

todo_include_todos = True

# source_suffix = {
#     '.rst': 'restructuredtext',
#     '.md': 'markdown',
# }

# latex_documents = [
#     (master_doc, 'project_name.tex', 'Project Name Documentation', 'Your Name', 'manual'),
# ]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
