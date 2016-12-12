from __future__ import unicode_literals

from django.db import models


# class Category(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return str(self.pk)

class Event(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    label = models.CharField(max_length=255)
    category = models.CharField(max_length=255)

    def __str__(self):
        return str(self.pk)
