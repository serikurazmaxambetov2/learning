from rest_framework import serializers

from .models import Lesson, Product

class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = ('name', 'author__first_name', 'start_time', 'price')

class LessonSerializer(serializers.ModelSerializer):
  class Meta:
    model = Lesson
    fields = ('name', 'video_url')