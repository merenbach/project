# README for Project

## Troubleshooting

### Permissions

Error rebuilding the Haystack index?  Maybe the `media` directory isn't owned by the server user (e.g., maybe it is owned by `root` instead of `www-data`).

### Memcached

- Please ensure that the memcached path is set correctly in settings.py.
- This may (or may not) be `unix:/var/run/memcached/memcached.pid` on CentOS
- This appears to actually be `unix:/var/run/memcached.pid` on Debian, something that I failed to discover for about a month.

### Configuration for MarsEdit

Use XML-RPC posting with aid of use MovableType *API*.  Select MovableType as blogging system for use of tags.

## Django compressor

We make use of a module from the dev branch.  This should be removed once it is integrated into the core.

- For Compressor to work, www-data user must have write access to the cache directory.
- The easiest way is to create this directory manually and make www-data the owner (although we could technically make www-data the group and root the owner, that might be more of a security hole)
- <http://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_STORAGE>

## TODO

- Remove outdated/unused CSS (sticky, normalize, handheld, antiscreen (?))

## Dependencies

Please see `requirements.txt` for required dependencies.

### Miscellaneous

- pip install django-maintenance
    - We are using [this version](https://github.com/steingrd/django-maintenance)
    - We were using [this version](https://github.com/thinkjson/django-maintenance)
- Our backup script is based upon
	- django-backup==1.0.1

## TODO

- Make sure we're using *only* the CSS files that we need
- Make sure that CSS files are included in the right order
- Add some additional ciphers (e.g., Chaocipher)
- Generate cipher forms using Django forms framework
- Can we benefit from setting TIME_FORMAT in settings?

## Bootstrap customizations

1. Install `nodejs` and `npm`
2. Run the following commands:

	npm update -g
	npm install -g less
	npm install -g uglify-js
	npm install -g jshint
	npm install -g recess
	npm install -g connect
	npm install -g hogan.js

### Scaffolding

#### For `merenbach.com`:

	@bodyBackground = #fafafa

#### For `theromantics.net`

	@bodyBackground = #cc9493;
	@sansFontFamily = 'Vollkorn', 'Palatino', 'Times', serif;

### Typography

    @baseFontSize = 18px (14 + 4)
    @baseLineHeight = 24px (20 + 4)
    @paddingLarge = 15px 23px (+4 +4)
    @paddingSmall = 6px 14px (+4 +4)
    @paddingMini = 5px 10px (+4 +4)
    @baseBorderRadius = 6px (4px + 4/2)
    @baseBorderRadius = 8px (6px + 4/2)
    @baseBorderRadiusSmall = 5px (3px + 4/2)

### Navbar

    @navbarHeight = 48px (40 + 2*4)

