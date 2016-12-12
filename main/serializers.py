from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    start = serializers.DateTimeField(required=True)
    end = serializers.DateTimeField(required=True)
    label = serializers.CharField(required=False,
                                  allow_blank=True,
                                  max_length=100)
    category = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Event
        fields = ('id', 'start', 'end', 'label', 'category')
