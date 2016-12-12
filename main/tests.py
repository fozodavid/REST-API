from django.test import TestCase
from django.http import HttpRequest
from rest_framework.test import RequestsClient
from datetime import datetime
from main.models import Event
from main.views import EventList


# Create your tests here.
class EventsTest(TestCase):

    def setUp(self):
        self.event_id = 65000
        self.event_start = "2016-12-15T10:00:00Z"
        self.ical_start = "20161215T100000Z"
        self.event_end = "2016-12-15T10:35:00Z"
        self.event_label = "This is a test"
        self.event_cat = "Red"

        self.post_dict = {
            'id': self.event_id,
            'start': self.event_start,
            'end': self.event_end,
            'label': self.event_label,
            'category': self.event_cat}

    def tearDown(self):
        Event.objects.get(pk=self.event_id).delete()

    def test_post_api_events(self):
        self.client.post('/api/events/', self.post_dict)
        m = Event.objects.get(pk=self.event_id)
        self.assertEquals(m.label, self.event_label)

    def test_get_api_events(self):
        Event.objects.create(**self.post_dict)
        client = RequestsClient()
        response = client.get('http://testserver/api/events/')
        for key in self.post_dict:
            self.assertIn(key, response.content.decode())

    def test_get_events_id(self):
        Event.objects.create(**self.post_dict)
        client = RequestsClient()
        response = client.get(
            'http://testserver/api/events/%s/' % self.event_id)
        for key in self.post_dict:
            self.assertIn(key, response.content.decode())

    def test_download_ics(self):
        Event.objects.create(**self.post_dict)
        client = RequestsClient()
        response = client.get('http://testserver/download/%s/' % self.event_id)
        self.assertIn('filename=export.ics',response.headers['Content-Disposition'])
        self.assertIn('BEGIN:VCALENDAR',response.content.decode())
        self.assertIn(self.ical_start, response.content.decode())
