# Paperbuzz

Django-paperbuzz is a simple Django app to display paperbuzz metrics.

Detailed documentation is in the "docs" directory.

## Quick start

1. Add "paperbuzz" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'paperbuzz',
    ]

2. Include the paperbuzz URLconf in your project urls.py like this::

    path('paperbuzz/', include('paperbuzz.urls')),

3. Run `python manage.py migrate` to create the paperbuzz models.

4. Visit http://127.0.0.1:8000/paperbuzz/10.1234/example.doi to view metrics.