RWGE bot as a django app because google hangouts chat bots have to be web services.

RWGE doesn't really need a database so django is overkill here, but I want to run him on my existing backend :)

Gchat doesn't support bots as well as I'd like (they only see messages if they are mentioned in them) so this is abandoned not fully finished.

Quick start
-----------

1. pip install git+git://github.com/rwgeaston/django-rwge

2. Add "rwge" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'rwge',
    ]

3. Include the rwge URLconf in your project urls.py like this::

    path('', include('rwge.urls')),


4. You might have some CSRF issues (I did)

5. Add this stuff to settings or local_settings:

    RWGE_URL = ''  # You choose something long

    RWGE_SECRET = '' # Google will provide when you create the bot service account

    PEOPLE_TO_ASK = ['tom', 'dick', 'harry']

    DEFAULT_MOTHER_FREQUENCY = 40

6. You may also want a "rwge" logger added to your loggers.

Here's what I did to get it running:

    https://github.com/rwgeaston/mario-stats-django/commit/da63e0ddcc494ba629c0bc20825d427d7a041d97
