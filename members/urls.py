from django.urls import path
from .views import *
from . import views

app_name = "customer"

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
    path('delete_task/<str:pk>/', views.deleteTask, name="delete_task"),

    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name="register"),

    path('about-us/', views.aboutDeveloper, name="about_us"),
    path('user-profile/', views.user_profile, name="user_profile"),

]