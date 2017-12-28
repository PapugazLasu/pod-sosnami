from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^([0-9]+)/$', views.detail, name = 'detail' ),
    url(r'^post_url/$', views.post_person, name='post_person' ),
    url(r'^user/(\w+)/$', views.profile, name='profile'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^like_person/$', views.like_person, name='like_person' ),
    url(r'^search/$', views.search, name='search'),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),
    ]
