from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from users import views as userviews
from projects import views as projectviews

urlpatterns = patterns('',
    url(r'users/$', userviews.UserList.as_view()),
    url(r'users/(?P<pk>[0-9]+)/$', userviews.UserDetail.as_view()),
    url(r'projects/$', projectviews.ProjectList.as_view()),
    url(r'projects/(?P<pk>[0-9]+)/$', projectviews.ProjectDetail.as_view()),
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
