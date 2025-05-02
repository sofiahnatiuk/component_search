from django.db import models
from django.contrib.auth.models import User


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
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Report(models.Model):
    component = models.ForeignKey("Component", on_delete=models.CASCADE, related_name="reports")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Report on {self.component.name} by {self.user.username}"
