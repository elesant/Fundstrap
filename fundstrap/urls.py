from django.conf.urls import patterns, include, url
from django.contrib import admin
from core.api import UserResource

admin.autodiscover()
user_resource = UserResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fundstrap.views.home', name='home'),
    # url(r'^fundstrap/', include('fundstrap.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(user_resource.urls)),
)
