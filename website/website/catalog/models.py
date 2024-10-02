from django.db import models


# Create your models here.
class Component(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.manufacturer} {self.name}"


class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)  # For subcategories

    def __str__(self):
        return self.name