from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    
    path("",views.index, name="home"),
    path("about",views.about, name="about"),
    path("service",views.service, name="service"),
    path("contact",views.contact, name="contact"),
    path("login/",views.loginView, name="login" ),
    path("user_signup/",views.user_signupview, name="user_signup" ),
    path("reporter_signup/",views.reporter_signupview, name="reporter_signup" ),
    path("upload/",views.news_upload, name="news_upload" ),
    
    
]