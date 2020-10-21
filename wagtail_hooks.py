from django.conf.urls import url
from django.templatetags.static import static
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _
from wagtail.admin.menu import MenuItem
from wagtail.core import hooks

from . import views


@hooks.register('register_admin_urls')
def register_admin_urls():
    return [
        url(r'^cache-management/$', views.index, name='cache_management'),
        url(r'^cache-management/clear_all_cache/$', views.clear_all_cache, name='clear_all_cache'),
    ]


@hooks.register('register_admin_menu_item')
def register_cache_management_menu_item():
    return MenuItem(
        _('Cache Management'),
        reverse('cache_management'),
        classnames='icon icon-help',
        order=1000
    )