from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=255)
    repo = models.URLField()

    contributors = models.ForeignKey('users.Profile', on_delete=models.DO_NOTHING)
    """
    Беру пример с github. 
    Эти ребята те, кто работают над проектом
    """

    def __str__(self):
        return self.name
