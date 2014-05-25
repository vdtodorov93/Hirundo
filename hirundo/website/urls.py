from django.conf.urls import patterns
from django.contrib.flatpages import views
from django.conf.urls import url


urlpatterns = patterns('website.views',
    url(r'^$', 'home', name="home"),
    url(r'^register/$', 'register', name='register'),
    url(r'^login/$', 'login', name='login'),
    url(r'^logout/$', 'logout', name='logout'),
    url(r'^users/$', 'users', name='users'),
    #url(r'^users', 'users', name="users"),
    #url(r'^messages', 'messages', name="messages"),
)
