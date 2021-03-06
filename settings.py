# -*- coding: utf-8 -*-

INSTALLED_ADDONS = [
    # <INSTALLED_ADDONS>  # Warning: text inside the INSTALLED_ADDONS tags is auto-generated. Manual changes will be overwritten.
    'aldryn-addons',
    'aldryn-django',
    'aldryn-sso',
    'aldryn-django-cms',
    'aldryn-devsync',
    'aldryn-bootstrap3',
    'aldryn-newsblog',
    'djangocms-googlemap',
    'djangocms-history',
    'djangocms-snippet',
    'djangocms-style',
    'djangocms-text-ckeditor',
    'djangocms-video',
    'django-filer',
    # </INSTALLED_ADDONS>
]

import aldryn_addons.settings
aldryn_addons.settings.load(locals())


# all django settings can be altered here

INSTALLED_APPS.extend([
    # add your project specific apps here
])

MIDDLEWARE_CLASSES.extend([
    # add your own middlewares here
])

CMS_TEMPLATES = (
    ('content.html', 'Home Page'),
    ('country-spotlight-page.html', 'Country Spotlight Page'),
    ('category-page.html', 'Section Category Page'),
    ('page-content.html', 'Section Page'),
    ('sub-section-page.html', 'Sub Section Page'),
    ('about.html', 'About Page'),
)
