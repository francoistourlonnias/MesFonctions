from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^travel/$', 'travel.views.index'),
    
# add the Hands On Exercise 10.1 URL pattern matching line here

    url(r'^travel/(?P<std_code>\d+)/$', 'travel.views.get_std_country')

)