from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Person(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='person_images',
                               default='media/default.png')
    likes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
