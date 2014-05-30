from django.conf.urls import patterns
from django.contrib.flatpages import views
from django.conf.urls import url


urlpatterns = patterns('website.views',
    url(r'^$', 'home', name="home"),
    url(r'^register/$', 'register', name='register'),
    url(r'^login/$', 'login', name='login'),
    url(r'^logout/$', 'logout', name='logout'),
    url(r'^users/$', 'users', name='users'),
    url(r'^follow/(?P<follow_user>\w+)$', 'follow', name='follow'),
    url(r'^unfollow/(?P<unfollow_user>\w+)$', 'unfollow', name='unfollow'),
    url(r'^messages/$', 'messages', name='messages'),
    url(r'^createmessage/$', 'createmessage', name='createmessage'),
    url(r'^about/$', 'about', name='about'),
    url(r'^contact/$', 'contact', name='contact'),
    url(r'^mymessages/$', 'mymessages', name='mymessages'),
    url(r'^mymessages/delete/(?P<message_id>\d+)$', 'delete_message_by_id', name='delete_message_by_id'),
)
