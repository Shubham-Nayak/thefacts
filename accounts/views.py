from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import BlogSpots,SliderImage
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import BlogSpotsForm
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
    form=BlogSpotsForm(request.POST or None, request.FILES or  None)
    if form.is_valid():
        obj=form.save(commit=False)
        obj.save()
        return redirect("/accounts/#dashboard")
    return render(request,"accounts/articals.html",{'form':form})
 


def edit(request,myid):
    
    obj=BlogSpots.objects.get(id=myid)
    form=BlogSpotsForm(request.POST or None,request.FILES or None,instance=obj)
    if form.is_valid():
        obj=form.save(commit=False)
        obj.save()
        return redirect("/accounts/#dashboard")

    return render(request,"accounts/editpost.html",{'form':form,'obj':obj})
   
def delete(request,myid):
    obj=BlogSpots.objects.get(id=myid)
    obj.delete()
    return redirect("/accounts/#dashboard")

    return render(request,"/accounts/#dashboard",{'obj':obj})   

def post(request,myurl):
    title=myurl.replace('-',' ')
    blog=BlogSpots.objects.filter(title=title)
    

    return render(request,"thenation/post.html",{"blogs":blog[0]})

  

   
   
   

       

