from django.urls import path

from .views import ProductListView, LessonListView


urlpatterns = [
  path('product-list/', ProductListView.as_view()),
  path('product/<int:pk>/', LessonListView.as_view())
]