from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from users import views as userviews
from projects import views as projectviews
from phases import views as phasesviews
from skills import views as skillviews
from allocations import views as allocationviews
from rest_framework.authtoken import views as authviews

urlpatterns = patterns('',
    url(r'^users/$', userviews.UserList.as_view(), name='users'),
    url(r'^users/(?P<pk>[0-9]+)/$', userviews.UserDetail.as_view(), name='users-detail'),
    url(r'^projects/$', projectviews.ProjectList.as_view(), name='projects'),
    url(r'^projects/(?P<pk>[0-9]+)/$', projectviews.ProjectDetail.as_view(), name='projects-detail'),
    url(r'^phases/$', phasesviews.PhaseList.as_view(), name='phases'),
    url(r'^phases/(?P<pk>[0-9]+)/$', phasesviews.PhaseDetail.as_view(), name='phases-detail'),
    url(r'^skills/$', skillviews.SkillList.as_view(), name='skills'),
    url(r'^skills/(?P<pk>[0-9]+)/$', skillviews.SkillDetail.as_view(), name='skills-detail'),
    url(r'^allocations/$', allocationviews.AllocationList.as_view(), name='allocations'),
    url(r'^allocations/(?P<pk>[0-9]+)/$', allocationviews.AllocationDetail.as_view(), name='allocations-detail'),
    url(r'^require-skill/$', phasesviews.RequireSkill.as_view(), name='require-skill'),
    url(r'^available-users/$', userviews.AvailableUser.as_view(), name='available-users'),
    url(r'^api-auth/$', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include('rest_framework_swagger.urls'), name='docs'),
    url(r'^login/$', userviews.LoginView.as_view(), name='login'),
    url(r'^$', projectviews.APIRoot.as_view(), name='index'),
)
urlpatterns = format_suffix_patterns(urlpatterns)
