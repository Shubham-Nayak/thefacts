from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from .models import BlogSpot,SliderImage,Contacts
from accounts.models import BlogSpots
from django.core.files.storage import FileSystemStorage #new
from math import ceil
from django.utils import timezone

# Create your views here.

def index(request):
    name=BlogSpots.objects.all().order_by('-time')
    slide=SliderImage.objects.all()
    update=BlogSpot.objects.all().order_by('-time')
    cat=BlogSpots.objects.values('catagory')
    allprod={'data':name,'image':slide,'cats':cat,'updates':update}
    return render(request,"thenation/index.html",allprod)


def about(request):
    return render(request,"thenation/about.html")

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        number=request.POST.get('number')
        query=request.POST.get('query')
        form=Contacts(name=name,email=email,phone=number,query=query)
        form.save()
        
    return render(request,"thenation/contact.html",{'msg':"Thanks For Contacting.."})

def admin(request):
    return render(request,"thenation/dashbord.html")

def post(request,myid):
    blog=BlogSpots.objects.filter(id=myid)
    return render(request,"thenation/post.html",{"blogs":blog[0]})

def posts(request,myid):
    blog=BlogSpot.objects.filter(id=myid)
    return render(request,"thenation/post.html",{"blogs":blog[0]})


'''def addslide(request):
    if request.method=="POST" and request.FILES['image']:
        desc=request.POST.get('desc')
        image=request.FILES['image']
              
        form=SliderImage(desc=desc,images=image)
        form.save()
    return render(request,"thenation/addslide.html")'''

'''def articals(request):
    if request.method == "POST" and request.FILES['image']:
        name=request.POST.get('name')
        title=request.POST.get('title')
        heading1=request.POST.get('heading1')
        content1=request.POST.get('content1')
        heading2=request.POST.get('heading2')
        content2=request.POST.get('content2')
        link=request.POST.get('links')
        time=time=timezone.datetime.now()
        images=request.FILES['image']
        thumbnil=request.FILES['thumbnils']
        form=BlogSpot(name=name,title=title,heading1=heading1,heading2=heading2,
        content1=content1,content2=content2,links=link,time=time,images=images,thumbnils=thumbnil)
        form.save()
    return render(request,"thenation/articals.html")

       

    return render(request,"thenation/articals.html")'''