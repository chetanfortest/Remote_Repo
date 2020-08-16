from django.db import models

# Create your models here.
class Movies(models.Model):
	name = models.CharField(max_length=30)
	language = models.CharField(max_length=30)
	url = models.URLField(max_length=200)
	image = models.ImageField(upload_to='images/') 
