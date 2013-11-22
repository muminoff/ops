from django.core.urlresolvers import resolve
from collections import OrderedDict


def menus(request):
    menus = OrderedDict([
        ('home_page', {'title': 'Home'}),
        ('papers_page', {'title': 'Papers'}),
        ('about_page', {'title': 'About'}),
        ('contrib_page', {'title': 'Contribution'}),
    ])

    try:
        name = resolve(request.path).url_name
        if name in menus:
            menus[name]['active'] = True
    except:
        pass

    return {
        'menus': menus,
    }
