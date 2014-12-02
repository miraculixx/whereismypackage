from django.conf.urls import patterns, include, url
from django.contrib import admin

import locator


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'whimpy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include(locator.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
