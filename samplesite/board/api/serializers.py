from rest_framework import serializers
from ..models import Board, Rubric


class RubricSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rubric
        fields = ['id', 'name']


class BoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Board
        fields = ['id', 'title', 'content', 'price', 'contacts', 'published', 'rubric', 'user']
