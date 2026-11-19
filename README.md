# Quillmark Site Starter

A small dependency-free static starter for academic personal sites, maintained
by the Quillmark theme group.

## Layout

- `site/` - content and site data for the individual site
- `theme/quillmark/` - shared theme: templates, styles and theme options
- `build.py` - renders `site/` into `_site/` with the Quillmark theme

## Quick start

    python build.py

Set the identity block in `site/_data/site.json`, then edit `site/index.md`.

The rendered output is written to `_site/`.

No build dependencies are required beyond Python 3.

Theme options live in `theme/quillmark/_config.yml`.

## Configurable profile header

The header can show an avatar, social links and an affiliation line.
Adjust the options in the theme configuration file.

Screenshots are generated from the sample site.
