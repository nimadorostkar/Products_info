from django.db import models
from django.utils.html import format_html
from django_resized import ResizedImageField

class Advertise(models.Model):
    name = models.CharField(max_length=256)
    image = ResizedImageField(size=[200, 200], default='advertise/default.png', upload_to='advertise')

    def __str__(self):
        return str(self.name)

    def img(self):
        return format_html("<img style='width:30px;' src='{}'>".format(self.image.url))
