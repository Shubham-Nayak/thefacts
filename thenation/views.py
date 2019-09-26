from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from .models import BlogSpot,SliderImage,Contacts,BrekingNews,Video
from accounts.models import BlogSpots
from django.core.files.storage import FileSystemStorage #new
from math import ceil
from django.utils import timezone 
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
import datetime


# Create your views here.

def index(request):
    name_list=BlogSpots.objects.all().order_by('-time')
    slide=SliderImage.objects.all()
    video=Video.objects.all().order_by('-time')
    update=BlogSpot.objects.all().order_by('-time')
    cat=BlogSpots.objects.values('catagory')
    currenttime = datetime.datetime.now().strftime('%H:%M:%S')
    brekingnews=BrekingNews.objects.all()

    #pagination
    paginator=Paginator(name_list,8)
    page = request.GET.get('page')
    try:
        name = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        name = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        name= paginator.page(paginator.num_pages)

    allprod={'data':name,'image':slide,'cats':cat,'updates':update,'currenttime':currenttime,'brekingnews':brekingnews,'video':video}
    return render(request,"thenation/index.html",allprod)


def about(request):
    return render(request,"thenation/about.html")



def contact(request):
    
    if request.method=="POST":
        
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        query=request.POST.get('query')
        
        contact=Contacts(name=name,email=email,phone=phone,query=query)
        contact.save()
        return render(request,"thenation/contact.html",{'error':'Thanks For Contacting..'})
    else:
        return render(request,"thenation/contact.html")
    


def admin(request):
    return render(request,"thenation/dashbord.html")

def post(request,myurl):
   
    title=myurl.replace('-',' ')
    blog=BlogSpots.objects.filter(title=title)
    recom=BlogSpots.objects.all()
    return render(request,"thenation/post.html",{"blogs":blog[0],"recom":recom})

def posts(request,myurl):
    title=myurl.replace('_',' ')
    blog=BlogSpot.objects.filter(title=title)
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