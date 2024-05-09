

import sys
sys.path.append('C://users/jegrami.de/blog/m.css/plugins')



AUTHOR = 'Jeremiah Igrami'
SITENAME = 'jegrami'
SITEURL = ""


M_BLOG_NAME = 'Articles'
M_BLOG_URL = 'articles/'

M_SITE_LOGO_TEXT = 'jegrami'

M_LINKS_NAVBAR1 = [('Home', '/', 'home', []),
                   ('Articles', 'articles/', 'articles', [ ]),
                   ('About', 'about/', 'about', []),
                   ('Github', 'https://github.com/jegrami', '', []) 
                   ]

M_LINKS_FOOTER3 = [('Contact', ''),
                   ('E-mail', 'mailto:jegrami.de@gmail.com'),
                   ('GitHub', 'https://github.com/jegrami'),
                   ('LinkedIn', 'https://www.linkedin.com/in/jeremiah-igrami'),
                   ('Twitter', 'https://twitter.com/je_grami')
                   ]


M_HIDE_ARTICLE_SUMMARY = True


PATH = 'content'

ARTICLE_PATHS = ['articles']
PAGE_PATHS = ['']
# ARTICLE_EXCLUDES = ['articles/authors', 'articles/categories', 'articles/tags']

STATIC_URL = '{path}'
STATIC_PATHS = ['static']

TIMEZONE = 'Africa/Lagos'

DEFAULT_LANG = 'en'

THEME = 'm.css/pelican-theme'
THEME_STATIC_DIR = 'static'
DIRECT_TEMPLATES = ['archives', 'categories']

M_CSS_FILES = ['https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,400i,600,600i%7CSource+Code+Pro:400,400i,600',
               '/static/m-dark.css']
M_THEME_COLOR = '#22272e'

PLUGIN_PATHS = ['m.css/plugins']

PLUGINS = ['m.abbr',
           'm.alias',
           'm.code',
           'm.components',
           'm.dox',
           'm.dot',
           'm.filesize',
           'm.gl',
           'm.gh',
           'm.htmlsanity',
           'm.images',
           'm.link',
           'm.math',
           'm.metadata',
           'm.plots',
           'm.sphinx',
           'm.qr',
           'm.vk']

FORMATTED_FIELDS = ['summary', 'landing', 'header', 'footer', 'description', 'badge']

HTMLSANITY_SMART_QUOTES = True
M_HTMLSANITY_HYPHENATION = True
M_HIDE_ARTICLE_SUMMARY = True
M_COLLAPSE_FIRST_ARTICLE = True

M_NEWS_ON_INDEX = ("My most recent articles", 3)

M_FINE_PRINT = """
jegrami. Copyright © `Jeremiah Igrami <mailto:jegrami.de@gmail.com>`_, 2024.
Made with `Pelican <https://getpelican.com>`_ and m.css.
"""

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
ARCHIVES_URL = 'articles/'
ARCHIVES_SAVE_AS = 'articles/index.html'
ARTICLE_URL = '{slug}/' 
ARTICLE_SAVE_AS = '{slug}/index.html'
AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None



# Blogroll

# PAGINATED_TEMPLATES = {'archives': True, 'tag': None, 'category': None, 'author': None}

DEFAULT_PAGINATION = 10

CACHE_CONTENT = False
LOAD_CONTENT_CACHE = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True