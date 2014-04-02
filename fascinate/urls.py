from django.conf.urls import patterns, url

from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns('fascinate.views',
    # url(r'^$', 'django_apps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^(?P<img_id>\d+)/$', 'post'),
    url(r'^upload/$', 'upload'),
    # API
    url(r'^api/(?P<img_id>\d+)/$', 'api_get_post'),
    url(r'^api/vote/(?P<img_id>\d+)/$', 'api_get_post_vote'),
    url(r'^api/recent/$', 'api_recent'),
    url(r'^api/popular/$', 'api_popular'),
)
