from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name

class Person(models.Model):
    p_name = models.CharField(max_length=250)
    p_img = models.ImageField(upload_to='pics')
    p_desc = models.TextField()
    def __str__(self):
        return self.p_name