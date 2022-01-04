from django.db import models

from decimal import Decimal

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name=models.CharField(max_length=60)
    friendly_name = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Ticket(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=16, null=True, blank=True)
    name=models.CharField('Ticket Name', max_length=60)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=3, decimal_places=0)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
