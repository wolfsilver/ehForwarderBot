#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# EH Forwarder Bot documentation build configuration file, created by
# sphinx-quickstart on Tue Feb 28 10:17:32 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

import sphinx.application
import sphinx_readable_theme

sys.path.insert(0, os.path.abspath('..'))

__version__ = "0.0.0"

exec(open('../ehforwarderbot/__version__.py').read())

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.todo',
              'sphinx.ext.viewcode',
              'sphinx.ext.githubpages',
              'sphinx.ext.napoleon']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'EH Forwarder Bot'
copyright = '2017 — 2018, Eana Hufwe'
author = 'Eana Hufwe'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.

version = ".".join(__version__.split(".")[:2])
# The full version, including alpha/beta/rc tags.
release = __version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `to\do` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
# html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']
# html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]


html_theme_path = [sphinx_readable_theme.get_html_theme_path()]
html_theme = 'readable'

# import sphinx_py3doc_enhanced_theme
# html_theme = "sphinx_py3doc_enhanced_theme"
# html_theme_path = [sphinx_py3doc_enhanced_theme.get_html_theme_path()]

# sys.path.append(os.path.abspath('_themes'))
# html_theme_path = ['_themes']
# html_theme = 'kr'

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'ehForwarderBotDoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'ehForwarderBot.tex', 'EH Forwarder Bot Documentation',
     'Eana Hufwe', 'manual'),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'ehforwarderbot', 'EH Forwarder Bot Documentation',
     [author], 1)
]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'ehForwarderBot', 'EH Forwarder Bot Documentation',
     author, 'ehForwarderBot', 'One line description of project.',
     'Miscellaneous'),
]

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True

# Sphinx-intl esttings
locale_dirs = ['locale/']   # path is example but recommended.
gettext_compact = False     # optional.


conversion = {
    'az': 'az_AZ', 'es': 'es_VE', 'id': 'id_ID',
    'it': 'it_IT', 'ja': 'ja_JP', 'ms': 'ms_MY',
    'ro': 'ro_RO', 'tr': 'tr_TR', 'zh': 'zh_CN',
    'en': 'en_US'
}


# Locale fallback settings
def locale_fallback_decorator(fun):

    def wrapper(self, **kwargs):
        self.config.language = conversion.get(self.config.language, self.config.language)
        return fun(self, **kwargs)
    return wrapper


sphinx.application.Sphinx._init_i18n = locale_fallback_decorator(sphinx.application.Sphinx._init_i18n)


def setup(self):
    self.config.language = conversion.get(self.config.language, self.config.language)
    self.config.overrides['language'] = conversion.get(self.config.overrides.get('language', None),
                                               self.config.overrides.get('language', None))
