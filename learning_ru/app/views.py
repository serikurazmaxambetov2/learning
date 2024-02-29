from rest_framework.generics import ListAPIView, RetrieveAPIView

from datetime import datetime

from .models import Lesson, Product
from .serializers import LessonSerializer, ProductSerializer


class ProductListView(ListAPIView):
  serializer_class = ProductSerializer
  
  def get_queryset(self):
    now = datetime.now()
    return Product.objects.filter(start_time__gt = now)

class LessonListView(ListAPIView):
  serializer_class = LessonSerializer

  def get_queryset(self):
    return Lesson.objects.filter(product__pk = self.kwargs['pk'])
  