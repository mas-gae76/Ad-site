from rest_framework import serializers
from .models import Board


class BoardSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    image = serializers.ImageField()
    content = serializers.CharField()
    price = serializers.IntegerField()
    contacts = serializers.CharField(max_length=15)
    published = serializers.DateTimeField()
    user = serializers.CharField()
    rubric = serializers.CharField()

    def create(self, validated_data):
        return Board.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.image = validated_data.get('image', instance.image)
        instance.content = validated_data.get('content', instance.content)
        instance.price = validated_data.get('price', instance.price)
        instance.contacts = validated_data.get('contacts', instance.contacts)
        instance.published = validated_data.get('published', instance.published)
        instance.user = validated_data.get('user', instance.user)
        instance.save()
        return instance
