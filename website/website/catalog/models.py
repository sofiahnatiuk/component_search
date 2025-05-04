from django.db import models
from django.contrib.auth.models import User


class Component(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    favorited_by = models.ManyToManyField(User, related_name='favorite_components', blank=True)

    package_type = models.CharField("Тип корпусу", max_length=100, null=True, blank=True)
    operating_voltage = models.DecimalField("Робоча напруга (V)", max_digits=10, decimal_places=2, null=True, blank=True)
    operating_current = models.DecimalField("Робочий струм (A)", max_digits=10, decimal_places=3, null=True, blank=True)
    power = models.DecimalField("Потужність (W)", max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.manufacturer} {self.name}"



class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)  # For subcategories
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def total_component_count(self):
        count = self.component_set.count()
        for child in self.category_set.all():
            count += child.total_component_count
        return count


class Report(models.Model):
    component = models.ForeignKey("Component", on_delete=models.CASCADE, related_name="reports")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Report on {self.component.name} by {self.user.username}"
