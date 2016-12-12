import os
import tempfile
from datetime import datetime

from django.http import Http404, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from icalendar import Calendar

from main.models import Event
from main.serializers import EventSerializer


def download_event(request, id):
    event = Event.objects.get(pk=id)
    file_path = os.path.join(tempfile.mkdtemp(), 'export.ics')

    cal = Calendar()
    cal['uid'] = event.id
    cal.add('dtstart', event.start)
    cal.add('dtend', event.end)
    cal['summary'] = event.label
    cal['category'] = event.category

    with open(file_path, 'wb') as f:
        f.write(cal.to_ical())

    with open(file_path, 'rb') as f:
        response = HttpResponse(
            f.read(), content_type="application/force-download")
        response['Content-Disposition'] = 'inline; filename=' + \
            os.path.basename(file_path)
        return response


class EventList(APIView):
    """
    Lists all events, or create a new snippet.
    """

    def get(self, request, format=None):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        pattern = "%Y-%m-%dT%H:%M:%SZ"
        request.data['start'] = strptime(request.data['start'], pattern)
        request.data['end'] = strptime(request.data['end'], pattern)
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        try:
            return Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        event = self.get_object(pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)
