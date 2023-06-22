
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import login
from home.models import user_data,upload
from django.contrib.auth import authenticate
# Create your views here.
def index(request):
   
    #return HttpResponse("this is home page")
    return render(request,"index.html")

def about(request):
    return HttpResponse("this is about page")

def service(request):
    return HttpResponse("this is sevices page")

def contact(request):
    return HttpResponse("this is contact page")

def create(request):
     return render(request,"signup/user_signup.html")
 
def reporter_signupview(request):
       return render(request, "signup/repoter_signup.html")


def loginView(request):
    
    b=user_data.objects.all().values()
    if request.method == "POST":
        email = request.POST.get('name')
        password = request.POST.get('password')
        for i in range(len(b)):
            
            if(b[i]['email']==email and b[i]['password']==password):
              data = login(email=email, password=password)
              print(data)
              data.save()
              b=user_data.objects.all().values()
             
              
              return redirect('home')
            
  
    return render(request,"login.html", {'upload':b }) 

def user_signupview(request):
    print("dhqwhdq")
    print(request.method)
    if request.method == "POST":
       
        firstname = request.POST.get('firstName')
        midlename = request.POST.get('midelname')
        lastname = request.POST.get('lastname')
        gender = request.POST.get('inlineRadioOptions')
        birth = request.POST.get('birth')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
      
        data = user_data(firstname = firstname, midlename=midlename, lastname=lastname, gender=gender,  birth= birth, email=email, phone=phone, password=password)
        data.save()
        return redirect('login')
        
    else:
        print("helloo")
        
    return render(request,"signup/user_signup.html")

def news_upload(request):
    beta=upload.objects.all().values()
    if request.method == "POST":
        image = request.POST.get('image')
        heading = request.POST.get('heading')
        news = request.POST.get('news')
      
        data = upload(file=image, heading=heading, news=news)
        data.save()
        beta=upload.objects.all().values()
        return redirect('home')
        
    return render(request,"upload.html",{'upload':beta })

def index(request):
    data=upload.objects.all()
    data1=login.objects.all()
    return render(request, "index.html",{"data": data , "data1":data1})


