Website for hackerspace.edu.pl
===================

This repo holds the website content for https://hackerspace.edu.pl.

Contributing
------------

To contribute to this repo, make sure that your main branch is up to
date and create a new branch from there.

The website content is in ``source/``.

Develop locally
~~~~~~~~~~~~~~~

This Python-based project uses `uv <https://docs.astral.sh/uv/>`__ and
`make <https://www.gnu.org/software/make/>`__, so install those first if
you don’t have them already.

1. Install dependencies

   ::

      uv sync

2. Build the site

   ::

      make html

   The output files are in the ``build/html/`` directory as HTML.

   Some warnings may be visible, but if the output ends with "build succeeded" then the website was built.

3. (optional) Preview the files with ``python -m http.server -d build/html/``.
