from django.shortcuts import render,redirect,HttpResponse
from .models import blood
from .forms import addmyform,createuserform
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def loginuser(request):
    if request.method=='POST':
        username = request.POST['name']
        password = request.POST['pp']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect ('/home')
        else:
            messages.info(request,"invalid username or password")
        
    return render(request,'login.html')

 
def logoutuser(request):
    logout(request)
    return redirect ('/')
      
def home(request):
    model=addmyform()
    modela=blood.objects.all()
    if request.method=="POST":
        form=addmyform(request.POST)
        form.save()
        return redirect('/')
    return render(request,'index.html',{'model':model,'modela':modela})

def delete(request,id):
    modela=blood.objects.get(id=id)
    modela.delete()
    return redirect('/')  



def update(request,id):
    modelo=blood.objects.get(id=id)
    model=addmyform(instance=modelo)
    modela=blood.objects.all()
    if request.method=="POST":
        formo=addmyform(request.POST,instance=modelo)
        formo.save()
        return redirect("/")
    return render(request,'index.html',{'model':model,'modela':modela})

def choose(request,dog):
    modela=blood.objects.filter(Q(Bloodgroup=dog))
    model=addmyform()
    if request.method=="POST":
        form=addmyform(request.POST)
        form.save()
        return redirect('/')
    return render(request,'index.html',{'model':model,'modela':modela})

def check(request):
    model=blood.objects.filter(Q(datediff="Available"))
    return render(request,'index.html',{'model':model})

def search(request):
    if request.method=="GET":
        jimmi=request.GET.get('search')
        modela=blood.objects.filter(Q(Fname=jimmi))
        return render(request,'index.html',{'modela':modela})    
  
  
  
'''  
def signupuser(request):
    modulo=myform()
    modella=signupform.objects.all()
    if request.method=='POST':
        fm=myform(request.POST)
        if fm.is_valid():
            fm.save()
        return redirect('/')
    return render(request,'signupform.html',{'modulo':modulo})'''
    
def signupuser(request):
    form=createuserform(request.POST)
    if form.is_valid():
        form.save()
        user=form.cleaned_data.get('username')
        messages.success(request,'Account was created for'+user)
        return redirect('/home')
    
    return render(request,'signupform.html',{'form':form})

       























 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
    
"""def A(request):
    model=addmyform()
    modela=blood.objects.filter(Q(Bloodgroup='A+ve'))
    if request.method=="POST":
        form=addmyform(request.POST)
        form.save()
        return redirect('/')
    return render(request,'index.html',{'model':model,'modela':modela})

def B(request):
    model=addmyform()
    modela=blood.objects.filter(Q(Bloodgroup='B+ve'))
    if request.method=="POST":
        form=addmyform(request.POST)
        form.save()
        return redirect('/')
    return render(request,'index.html',{'model':model,'modela':modela})

def AB(request):
    model=addmyform()
    modela=blood.objects.filter(Q(Bloodgroup='AB+ve'))
    if request.method=="POST":
        form=addmyform(request.POST)
        form.save()
        return redirect('/')
    return render(request,'index.html',{'model':model,'modela':modela})

def O(request):
    model=addmyform()
    modela=blood.objects.filter(Q(Bloodgroup='O+ve'))
    if request.method=="POST":
        form=addmyform(request.POST)
        form.save()
        return redirect('/')
    return render(request,'index.html',{'model':model,'modela':modela})

def delete(request,id):
    modela=blood.objects.get(id=id)
    modela.delete()
    return redirect('/')  



def update(request,id):
    modelo=blood.objects.get(id=id)
    model=addmyform(instance=modelo)
    modela=blood.objects.all()
    if request.method=="POST":
        formo=addmyform(request.POST,instance=modelo)
        formo.save()
        return redirect("/")
    return render(request,'index.html',{'model':model,'modela':modela}) """
    





     