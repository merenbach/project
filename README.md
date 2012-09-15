# README for Project

## Configuration for MarsEdit
Use XML-RPC posting with aid of use MovableType *API*.  Select MovableType as blogging system for use of tags.

## TODO
- Remove outdated/unused CSS (sticky, normalize, handheld, antiscreen (?))

## Dependencies
- pip install django-maintenance
    - We are using [this version](https://github.com/steingrd/django-maintenance)
    - We were using [this version](https://github.com/thinkjson/django-maintenance)
- django-analytical==0.13.0
- django-analytical==0.5
- django-backup==1.0.1
- django-blog-zinnia==0.11.2
- django-breadcrumbs==1.1.1
- django-compressor==1.2
- django-dajax==0.9.2
- django-dajaxice==0.5.2
- django-disqus==0.4.1
- django-haystack==1.2.7
- django-maintenance==0.1
- django-markdown==0.1.0
- django-mollom==0.1.1
- django-mptt==0.5.4
- django-photologue==2.4
- django-sekizai==0.6.1
- django-tagging==0.3.1
- django-xmlrpc==0.1.4
- linaro-django-pagination==2.0.2

## Older Dependencies
- pip install django-google-analytics
    - We are using [this version](http://pydoc.net/django_google_analytics/latest/)
    - This version is different from the one that we had been using
    - It differs from [this version](http://code.google.com/p/django-google-analytics/)

## TODO
- Make sure we're using *only* the CSS files that we need
- Make sure that CSS files are included in the right order
