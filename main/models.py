from django.db import models


# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=225)
    short_description = models.CharField(max_length=225)
    long_description = models.CharField(max_length=5000)

    def __str__(self):
        return self.name


class Images(models.Model):
    isMain = models.BooleanField()
    isSvg = models.BooleanField()
    src = models.CharField(max_length=500)

    def __str__(self):
        return self.src
