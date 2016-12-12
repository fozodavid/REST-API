from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    start = serializers.DateTimeField(required=True)
    end = serializers.DateTimeField(required=True)
    label = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    category = serializers.CharField(
        required=False, allow_blank=True, max_length=100)

    def create(self, validated_data):
        return Event.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.start = validated_data.get('start', instance.start)
        instance.end = validated_data.get('end', instance.end)
        instance.label = validated_data.get('label', instance.label)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance

    class Meta:
        model = Event
        fields = ('id', 'start', 'end', 'label', 'category')
