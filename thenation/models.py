from django.db import models

# for adding slides
class SliderImage(models.Model):
    id=models.AutoField(primary_key=True) 
    images= models.ImageField()
    desc=models.CharField(max_length=50,default="")    

    def __str__(self):
        return self.desc

class Video(models.Model):
    id=models.AutoField(primary_key=True) 
    link=models.CharField(max_length=1000)
    desc=models.CharField(max_length=50,default="")  
    time=models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.desc
    class Meta:
        ordering=['-time']

class BlogSpot(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30,default="")
    title=models.CharField(max_length=100,default="")
    heading1=models.CharField(max_length=100,default="")
    heading2=models.CharField(max_length=150,default="")
    content1=models.TextField(max_length=2500,default="")
    content2=models.TextField(max_length=2500,default="")
    links=models.CharField(max_length=500,default="",blank=True)
    catagory=models.CharField(max_length=30,default="")
    time=models.DateTimeField(auto_now_add=True)
    
    keywords=models.CharField(max_length=1000)

    images=models.ImageField(default="")
    thumbnils=models.ImageField(default="")
    #video=models.ImageField(upload_to="thenation/video",default="")

    def time_pretty(self):
        return self.time.strftime('%d %e , %Y')
    
    class Meta:
        ordering=['-time']

    def __str__(self):
        return self.title
    
    def title_url(self):        
        return self.title.replace(' ','-')
       
    
class Contacts(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=300)
    phone=models.IntegerField(default=0)    
    query=models.CharField(max_length=50,default="")
    
    def __str__(self):
        return self.name

class BrekingNews(models.Model):
    id=models.AutoField(primary_key=True)
    
    title=models.CharField(max_length=100,default="")
    
    time=models.DateTimeField()
    
    

   
    #video=models.ImageField(upload_to="thenation/video",default="")

    def time_pretty(self):
        return self.time.strftime('%d %e , %Y')
    
    class Meta:
        ordering=['-time']

    def __str__(self):
        return self.title
