from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=100)
    creator = models.CharField(max_length=50)
    country_of_origin = models.CharField(max_length=50)

    def __str__(self):
        return self.name
