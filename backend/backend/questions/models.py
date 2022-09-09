from distutils.command.upload import upload
from django.db import models
from themes.models import Theme
# Create your models here.
class Question(models.Model):
    choices = (
        ('easy','easy'),
        ('medium','medium'),
        ('hard','hard')
    )
    theme = models.ForeignKey(Theme,on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    right_answer = models.OneToOneField('Answer',on_delete=models.CASCADE)
    wrong_answer = models.OneToOneField('Answer',related_name='default',on_delete=models.CASCADE)
    difficulty = models.CharField(max_length =10,choices=choices , default='easy')
    pic = models.ImageField(upload_to='questions_pic' , default=None , null=True , blank =True)
    def __str__(self):
        return self.text
class Answer(models.Model):
    text = models.CharField(max_length=100)
    def __str__(self):
        return self.text