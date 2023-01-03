from django.db import models

# Create your models here.

class Imageo(models.Model):
    file = models.ImageField(upload_to='cropped_images')
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)


class userLogin(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    instuation = models.CharField(max_length=500, blank=True, null=True)
    position = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True, unique=True)
    emisurl = models.CharField(max_length=300, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    password = models.CharField(max_length=400, blank=True, null=True)

    def __str__(self):
        return self.name