from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SliderImage(models.Model):
    id=models.AutoField(primary_key=True) 
    images=models.ImageField(default="")
    desc=models.CharField(max_length=50,default="")    

    def __str__(self):
        return self.desc


class BlogSpots(models.Model):
  
    
    id=models.AutoField(primary_key=True)
    name=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=300,error_messages={'required': 'Please enter your name'})
    
    heading1=models.CharField(max_length=250,default="")
    heading2=models.CharField(max_length=250,default="")
    content1=models.TextField(max_length=25500,default="")
    content2=models.TextField(max_length=25500,default="")
    keywords=models.CharField(max_length=1000)
    links=models.CharField(max_length=500,default="",blank=True)
    catagory=models.CharField(max_length=30,default="")
    time=models.DateTimeField(auto_now_add=True)
    
    

    images=models.FileField()
    thumbnils=models.FileField()
    #video=models.ImageField(upload_to="thenation/video",default="")

    def summary(self):
        return self.body[:100]

    def time_pretty(self):
        return self.time.strftime('%d %e , %Y')
        
    def title_url(self):  
      
        return self.title.replace(' ','-')
    
    class Meta:
        ordering=['-time']

    def __str__(self):
        return self.title
    