#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Emmanuel I. Obi'
SITENAME = 'blog'
SITEURL = 'http://withtwoemms.github.io/blog'

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Pythonic Perambulations', 'http://jakevdp.github.io/'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/manualautomaton'),
          ('instagram', 'https://www.instagram.com/wellmanwell/'),)

DEFAULT_PAGINATION = 10

TWITTER_USERNAME = 'manualautomaton'

THEME = 'themes/pelican-alchemy/alchemy'

SITESUBTITLE = 'Radiative transfer is a thing that happens.'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
