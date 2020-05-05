from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='registerUser'
urlpatterns = [

    #homepage
    path('', views.index, name='index'),

    #user register,login,logout
    path('registerUser/', views.registerUser, name='registerUser'),
    path('user_logout/', views.user_logout, name='logout'),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name='login.html'),
         name='login'),
               ]
#redirect_authenticated_user=True is used for prevent the re-login to server when already that person is logged in
