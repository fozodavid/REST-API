from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import EventList, EventDetail

app_name = 'main'

urlpatterns = [
    url(r'^events/', EventList.as_view(),
        name='event_list'),
    url(r'^events/(?P<id>\d+)$',
        EventDetail.as_view(),
        name='event_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
