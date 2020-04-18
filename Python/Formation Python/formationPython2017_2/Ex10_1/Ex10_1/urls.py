from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Ex10_1_Done.views.home', name='home'),
    # url(r'^Ex10_1_Done/', include('Ex10_1_Done.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
        url(r'^airline/$', 'airline.views.index'),
    
# add the Hands On Exercise 10.1 URL pattern matching line here


)
