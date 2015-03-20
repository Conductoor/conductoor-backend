from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from users import views as userviews

urlpatterns = patterns('',
    url(r'users/$', userviews.UserList.as_view()),
    url(r'users/(?P<pk>[0-9]+)/$', userviews.UserDetail.as_view()),
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
