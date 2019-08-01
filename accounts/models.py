from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SliderImage(models.Model):
    id=models.AutoField(primary_key=True) 
    images=models.ImageField(upload_to="thenation/images",default="")
    desc=models.CharField(max_length=50,default="")    

    def __str__(self):
        return self.desc


class BlogSpots(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100,default="")
    heading1=models.CharField(max_length=100,default="")
    heading2=models.CharField(max_length=150,default="")
    content1=models.TextField(max_length=500,default="")
    content2=models.TextField(max_length=500,default="")
    links=models.CharField(max_length=500,default="")
    catagory=models.CharField(max_length=30,default="")
    time=models.DateTimeField()
    
    

    images=models.ImageField(upload_to="thenation/images",default="")
    thumbnils=models.ImageField(upload_to="thenation/images",default="")
    #video=models.ImageField(upload_to="thenation/video",default="")

    def summary(self):
        return self.body[:100]

    def time_pretty(self):
        return self.time.strftime('%d %e , %Y')
    
    class Meta:
        ordering=['-time']

    def __str__(self):
        return self.title
    