
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import user_data,upload,login, reporter,user_database
from .form import ImageForm

# from django.contrib.auth import login,authenticate
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
   


usertype="user"
def loginView(request):
    data1=login.objects.all()
    data1.delete()
    b=user_database.objects.all().values()
    global usertype
    if request.method == "POST":
        email = request.POST.get('name')
        password = request.POST.get('password')
        i=0
        j=0
        if(i<(len(b))):
            
            if(b[i]['email']==email and b[i]['password']==password):
              user=login(email=email, password=password)
              user.save()
              usertype=b[i]["usertype"]
              request.session["email"] = email
              request.session["password"] = password
              print(request.session["email"])
              print(request.session["password"])

              i=i+1
              return redirect("home")
    
    
    return render(request,"login.html")

def user_signupview(request):
    print("dhqwhdq")
    print(request.method)
    if request.method == "POST":
       
        firstname = request.POST.get('firstName')
        midlename = request.POST.get('midelname')
        lastname = request.POST.get('lastname')
        username=request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        address = request.POST.get('address', "default")
        school = request.POST.get('school', "default")
        collage=request.POST.get('college',"default")
        usertype = request.POST.get('usertype', "user")
      
        data = user_database(firstname = firstname, midlename=midlename, lastname=lastname,  email=email, phone=phone, password=password,adress=address, school=school, usertype=usertype, username=username, collage=collage)
        data.save()
        print("brt")
        return redirect('login')
        
    else:
        print("helloo")
        
    return render(request,"signup/user_signup.html")


def news_upload2(request):
    if request.method == "POST":
        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            print("helllo")
            form=ImageForm()
            img=upload.objects.all()
            return redirect("home")
    else:
        form=ImageForm()
        img=upload.objects.all()
        print("harsh")
    return render(request,"upload2.html",{"img":img,"form":form})

def index(request):
    
    
    data=upload.objects.all()
    data1=login.objects.all().values()
    if(len(data1)==1):
        email=data1[0]["email"]
        password=data1[0]["password"]
        data1=login.objects.all()
        print(usertype)
        return render(request, "index.html",{"data": data ,"email":request.session["email"], "password":password ,"type_of_user":usertype})
    else:
        return render(request, "index.html",{"data": data , "data1":len(data1)})

def my_news(request):
    # c=0
    
    type_of_user=usertype
    data=upload.objects.all()
    data1=login.objects.all().values()
    print(len(data1))
    form=ImageForm()
    img=upload.objects.all()
    if(len(data1)==1):
        email=data1[0]["email"]
        password=data1[0]["password"]
        data1=login.objects.all()
        
        return render(request, "my_news.html",{"data": data ,"email":email, "password":password ,"type_of_user":usertype, "img":img,"form":form})
    else:
        return render(request, "my_news.html",{"data": data , "data1":len(data1), "img":img,"form":form})


    
    

def logoutView(request):
    data1=login.objects.all()
    data1.delete()
    request.session["email"]="null"
    print(request.session.get('name'))
    return redirect('home')
    

    