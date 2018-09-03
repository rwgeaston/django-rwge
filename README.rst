RWGE bot as a django app because google hangouts chat bots have to be web services.

RWGE doesn't really need a database so django is overkill here, but I want to run him on my existing backend :)

Quick start
-----------

1. Add "rwge" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'rwge',
    ]

2. Include the rwge URLconf in your project urls.py like this::

    path('', include('rwge.urls')),

