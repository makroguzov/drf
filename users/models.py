from django.contrib.auth.models import AbstractUser
from django.db import models


class Profile(AbstractUser):
    email = models.EmailField(unique=True)


class Project(models.Model):
    name = models.CharField(max_length=255)
    repo = models.URLField(max_length=511, blank=True, default='')
    owner = models.ForeignKey(Profile, related_name='projects', on_delete=models.CASCADE)
    contributors = models.ManyToManyField(Profile,
                                          related_name='contributors', blank=True)
    """
    Беру пример с github. 
    Эти ребята те, кто работают над проектом.
    """

    def __str__(self):
        return self.name
