from django.contrib import admin
from django.urls import path,include
from home import views
from .views import index
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [ 
    path("",views.index, name="home"),
    path("index/",views.index, name="index"),
    
    path("about",views.about, name="about"),
    path("service",views.service, name="service"),
    path("contact",views.contact, name="contact"),
    path("login/",views.loginView, name="login" ),
    path("logout",views.logoutView, name="logout" ),
    path("user_signup/",views.user_signupview, name="user_signup" ),
    path("reporter_signup/",views.reporter_signupview, name="reporter_signup" ),
    path("upload/",views.news_upload2, name="news_upload2" ),
    path("my_news/",views.my_news, name="my_news" ),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)