from django.db import models

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name=models.CharField(max_length=60)
    friendly_name = models.CharField(max_length=60, null=True, blank=True)
    price = models.DecimalField(max_digits=4, decimal_places=0)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Package(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=16, null=True, blank=True)
    name=models.CharField(max_length=60)
    included = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
