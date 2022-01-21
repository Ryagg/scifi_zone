from django.db import models


class Category(models.Model):
    """A class for the different ticket and package categories"""


    class Meta:
        """Set the correct plural form"""
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=60)
    friendly_name = models.CharField(max_length=60, null=True, blank=True)
    price = models.DecimalField(
        null=True, blank=True, max_digits=4, decimal_places=0)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_friendly_name(self):
        """Improve readability by using the friendly_name of the category"""

        return self.friendly_name


class Ticket(models.Model):
    """A class for all tickets"""

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=16, null=True, blank=True)
    name = models.CharField(max_length=60)
    price_category = models.CharField(max_length=1, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=3, decimal_places=0)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    included = models.TextField(null=True, blank=True)
    ticketholder_name = models.CharField(max_length=60, null=True, blank=True)
    star = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Package(models.Model):
    """A class for all packages"""

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=16, null=True, blank=True)
    name = models.CharField(max_length=60)
    included = models.TextField(null=True, blank=True)

    def __str__(self):
        """Improves readability"""

        return str(self.name)


class Actor(models.Model):
    """A class for all convention guests"""

    name = models.CharField(max_length=60, null=True, blank=True)
    star_autograph_category = models.CharField(
        max_length=1, null=True, blank=True)
    star_photoshoot_category = models.CharField(
        max_length=1, null=True, blank=True)
    star_image_url = models.URLField(max_length=1024, null=True, blank=True)
    star_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.name)
