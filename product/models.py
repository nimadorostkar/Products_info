from django.db import models
from django.utils.html import format_html
from django_resized import ResizedImageField

class Category(models.Model):
    name = models.CharField(max_length=256, unique=True)
    def __str__(self):
        return str(self.name)

class Type(models.Model):
    name = models.CharField(max_length=256, unique=True)
    def __str__(self):
        return str(self.name)

class Product(models.Model):
    name = models.CharField(max_length=256)
    barcode = models.CharField(max_length=256, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    price = models.CharField(max_length=256, default=0)
    off_price = models.CharField(max_length=256, default=0)
    off_percent = models.CharField(max_length=256, default=0)
    image = ResizedImageField(size=[200, 200], default='products/default.png', upload_to='products')

    def __str__(self):
        return str(self.name)
    def img(self):
        return format_html("<img style='width:30px;border-radius:50%;' src='{}'>".format(self.image.url))
