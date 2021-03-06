"""shastri URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user import views as userview
from Post_UserInfo_comment import views as postview
from . import views

urlpatterns = [
    path('signup/' ,userview.SignUpView.as_view(),name='signup_form'),
    path('admin/', admin.site.urls),
    path('user/home/',postview.UserHome.as_view(),name='user_home'),
    path('login/', userview.LoginView.as_view(),name='login'),
    path('logout/', userview.Logout.as_view(),name='logout'),
    path('user/home/post/create/',postview.CreatePost.as_view(),name='create_post'),   
    path('',views.Home,name='home') ,

]
