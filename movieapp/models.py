from django.db import models

# Create your models here.
class Movies(models.Model):
    name = models.CharField(max_length=200,blank=True)
    desc = models.TextField(blank=True)
    year = models.IntegerField(null=True)
    img = models.ImageField(upload_to='gallery')
    def __str__(self):
        return self.name
