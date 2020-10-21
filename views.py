from django.shortcuts import render
from wagtail.core.models import Site
from django.urls import reverse
from wagtail.contrib.frontend_cache.utils import PurgeBatch

def index(request):
    # There should only ever be one instance of the guide
    # But we need to check the site incase there is a 'per' site guide
    # On a multisite setup
    return render(request, 'cache_management/base.html', {
        'content': 'test',
        'link': reverse('clear_all_cache')
    })


def clear_all_cache(request):
    pages = request.site.root_page.get_descendants(inclusive=True)
    batch = PurgeBatch()
    batch.add_pages(pages)
    batch.purge()
    return render(request, 'cache_management/base.html', {
        'pages': len(pages),
    })

