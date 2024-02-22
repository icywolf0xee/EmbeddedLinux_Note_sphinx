# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'EmbeddedLinux_Note_sphinx'
copyright = '2024, cumeni'
author = 'cumeni'
release = 'v1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []


source_suffix = '.rst'


html_sidebars = {
        '**': [
            'about.html',
            'navigation.html',
            'relations.html',
            'searchbox.html',
            'donate.html',
        ]
    }

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
#
# html_theme = 'alabaster'
html_theme='sphinx_rtd_theme'
html_static_path = ['_static']
