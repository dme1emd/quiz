from django.db import models

# Create your models here.
class Theme(models.Model):
    name = models.CharField(max_length=40)
    pic = models.ImageField(upload_to='themes_pic' , null=True,default=None,blank =True)
    def __str__(self):
        return self.name