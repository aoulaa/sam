from django.contrib.postgres.search import SearchVectorField
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    ref = models.CharField(max_length=50)
    search = SearchVectorField(null=True, blank=True)

    def __str__(self):
        return self.title
