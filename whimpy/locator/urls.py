from django.conf.urls import patterns, url, include

from locator import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'whimpy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', views.index),
)