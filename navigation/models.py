from django.db import models

# Create your models here.
class HomeImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='home',verbose_name='首页大图',null=True)
    

