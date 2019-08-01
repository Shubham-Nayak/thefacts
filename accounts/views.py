from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpRequest
from django.contrib.auth.models import User
from django.contrib import auth
from .models import BlogSpots,SliderImage
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
   if request.user.is_authenticated:
        
        artical=BlogSpots.objects.filter(name=request.user)
        #slide=SliderImage.objects.all()
       
        allprod={'data':artical}
    
        return render(request,"accounts/dashboard1.html",allprod)
   else:
        return render(request,"accounts/index.html",{'name':'shubham'})

def signup(request):
    if request.method=="POST":
        #user singnup
        if request.POST['pass1'] == request.POST['pass2']:
            try:
                User.objects.get(username=request.POST['username'])
                return render(request,"accounts/signup.html",{'error':'user alrady taken'})
            except Exception:
                user=User.objects.create_user(username=request.POST['username'],password=request.POST['pass1'],first_name=request.POST['firstname'],last_name=request.POST['lastname'],email=request.POST['email'])
                #auth.login(request,user)
                user.save()
                
                return render (request,'accounts/login.html')

                
        else:
            return render(request,"accounts/signup.html",{'error':'password not match'})
    else:
        return render(request,"accounts/signup.html")






def login(request):
    if request.method=="POST":
        user=auth.authenticate(username=request.POST['username'],password=request.POST['pass'])
        if user is not None:
            auth.login(request,user)
            #return render(request,'accounts/dashboard.html')
            return redirect('/accounts/')
        else:
            return render(request,'accounts/login.html',{'error':'username and password was incorrect'})




    else:
        return render(request,'accounts/login.html')

def logout(request):
    if request.method=='POST':
        auth.logout(request)
    return render(request,'accounts/index.html')



def addslide(request):
    if request.method=="POST" and request.FILES['image']:
        
        desc=request.POST.get('desc')
        image=request.FILES['image']
              
        form=SliderImage(desc=desc,images=image)
        form.save()
    return render(request,"accounts/addslide.html")
@login_required
def articals(request):
    if request.method == "POST" :
        #images=request.FILES['image']
        if request.POST['title'] and request.POST['heading1'] and request.POST['content1'] and request.POST['heading2'] and request.POST['content2'] and request.POST['category'] and request.POST['links'] and request.FILES['image'] and request.FILES['thumbnils'] :
            blog=BlogSpots()
            
            blog.title=request.POST['title']
            blog.heading1=request.POST['heading1']
            blog.content1=request.POST['content1']
            blog.heading2=request.POST['heading2']
            blog.content2=request.POST['content2']
            blog.catagory=request.POST['category']

            blog.links=request.POST['links']
            blog.time=timezone.datetime.now()
            blog.images=request.FILES['image']
            blog.thumbnils=request.FILES['thumbnils']
            blog.name=request.user
            blog.save()
            return redirect("/accounts/#dashboard")
            
        else:
            return render(request,"accounts/articals.html",{'error':"insert proper detail carefully "})
    return render(request,"accounts/articals.html")


def edit(request,myid):
    blog=BlogSpots.objects.filter(id=myid)
    return render(request,"accounts/editpost.html",{'data':blog[0]})

def post(request,myid):
    blog=BlogSpots.objects.filter(id=myid)
    

    return render(request,"thenation/post.html",{"blogs":blog[0]})

def update(request,myid):
    post=BlogSpots.objects.get(id=myid)
    if request.method=='POST':
        form=BlogSpots(request.POST or None, post)
        form.save()
        return redirect('/accounts/')
    return redirect('/accounts/')

   
   
   

       

