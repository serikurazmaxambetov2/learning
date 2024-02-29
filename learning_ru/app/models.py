from django.db import models
from django.contrib.auth.models import User

class BaseAbstractModel(models.Model):
  name = models.CharField(max_length = 100)
  
  def __str__(self):
    return self.name
  
  class Meta:
    abstract = True

# 1. Создать сущность продукта. У продукта должен быть
# создатель этого продукта(автор/преподаватель). 
# Название продукта, дата и время старта, стоимость (1 балл)
class Product(BaseAbstractModel):
  author = models.ForeignKey(User, on_delete = models.CASCADE, 
                             related_name = 'products', 
                             related_query_name = 'product')

  # 2. Определить, каким образом мы будем понимать, 
  # что у пользователя(клиент/студент) есть доступ к продукту. (2 балл)
  bought_users = models.ManyToManyField(User, 
                                        related_name = 'bought_products', 
                                        related_query_name = 'bought_product')
  #####

  start_time = models.DateTimeField()
  price = models.IntegerField()

# 3. Создать сущность урока. Урок может принадлежать только одному продукту.. 
# В уроке должна быть базовая информация: название, ссылка на видео. (1 балл)
class Lesson(BaseAbstractModel):
  video_url = models.URLField()
  product = models.ForeignKey(Product, on_delete = models.CASCADE, 
                              related_name = 'lessons', 
                              related_query_name = 'lesson')

# 4. Создать сущность группы. 
# По каждому продукту есть несколько групп пользователей, 
# которые занимаются в этом продукте. 
# Минимальное и максимальное количество юзеров в группе 
# задается внутри продукта. Группа содержит следующую 
# информацию: ученики, которые состоят в группе, название
# группы, принадлежность группы к продукту (2 балла)
class Group(BaseAbstractModel):
  product = models.ForeignKey(Product, on_delete = models.CASCADE, 
                              related_name = 'groups', 
                              related_query_name = 'group')
  users = models.ManyToManyField(User, related_name = 'product_groups', 
                                 related_query_name = 'product_group')
  users_count_min = models.IntegerField()
  users_count_max = models.IntegerField()
  
# python manage.py makemigrations && python manage.py migrate