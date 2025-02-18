from django.db import models
class people(models.Model):
    name=models.CharField(max_length=25)
    age=models.IntegerField()
    email=models.EmailField()
    mplace=models.CharField(max_length=25)
    mdate=models.CharField(max_length=25)
    cpn1=models.CharField(max_length=25)
    cpnum1=models.IntegerField()
    cpn2=models.CharField(max_length=25)
    cpnum2=models.IntegerField()
    fn=models.CharField(max_length=25)
    mn=models.CharField(max_length=25)
    gn=models.CharField(max_length=25)
    district=models.CharField(max_length=25)
    state=models.CharField(max_length=25)
    passwd=models.CharField(max_length=25)
    image=models.ImageField()
                       


# Create your models here.
