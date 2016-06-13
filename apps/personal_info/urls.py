from django.conf.urls import patterns, url

from .views import PersonalInfoDetail


urlpatterns = patterns(
    '',
    url(r'^$', PersonalInfoDetail.as_view(), name='personal_info'),
)
