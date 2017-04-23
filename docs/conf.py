#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Current preferred theme.
html_theme = "sphinx_py3doc_enhanced_theme"

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'jaraco.packaging.sphinx',
    'rst.linker',
]

master_doc = 'index'
autodoc_member_order = 'bysource'
intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}

if html_theme == 'sphinx_py3doc_enhanced_theme':
    import sphinx_py3doc_enhanced_theme
    html_theme_path = [sphinx_py3doc_enhanced_theme.get_html_theme_path()]
    html_theme_options = {
        'bodyfont': '"Lucida Grande",Arial,sans-serif',
        'headfont': '"Lucida Grande",Arial,sans-serif',
        'extrastyling': False,
    }

link_files = {
    '../CHANGES.rst': dict(
        using=dict(
            GH='https://github.com',
        ),
        replace=[
            dict(
                pattern=r'(Issue )?#(?P<issue>\d+)',
                url='{package_url}/issues/{issue}',
            ),
            dict(
                pattern=r'^(?m)((?P<scm_version>v?\d+(\.\d+){1,2}))\n[-=]+\n',
                with_scm='{text}\n{rev[timestamp]:%d %b %Y}\n',
            ),
            dict(
                pattern=r'PEP[- ](?P<pep_number>\d+)',
                url='https://www.python.org/dev/peps/pep-{pep_number:0>4}/',
            ),
        ],
    ),
}
