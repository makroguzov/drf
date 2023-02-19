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


class TODO(models.Model):
    class Status(models.TextChoices):
        OPEN = 'OPEN', 'Открыта'
        CLOSE = 'CLOSE', 'Закрыта'

    text = models.TextField()
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='todos')
    status = models.CharField(max_length=63,
                              choices=Status.choices,
                              default=Status.OPEN)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'todo <status: {self.status}>:- {self.text[:50]} {"..." if len(self.text) > 50 else ""}'
