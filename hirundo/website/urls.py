from django.conf.urls import patterns
from django.contrib.flatpages import views
from django.conf.urls import url


urlpatterns = patterns('website.views',
    url(r'^$', 'home', name="home"),
    url(r'^register/$', 'register', name='register')
    #url(r'^users', 'users', name="users"),
    #url(r'^messages', 'messages', name="messages"),
)
