from rest_framework import serializers
from main.models import Event


class EventSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    start = serializers.DateTimeField(required=True)
    end = serializers.DateTimeField(required=True)
    label = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    category = serializers.CharField(
        required=False, allow_blank=True, max_length=100)

    def create(self, validated_data):
        return Event.objects.create(**validated_data)

    class Meta:
        model = Event
        fields = ('id', 'start', 'end', 'label', 'category')
