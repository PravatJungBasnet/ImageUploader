from django.db import models

# Create your models here.
class Image(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='photo')
    
    date=models.DateField(auto_now_add=True)
 

