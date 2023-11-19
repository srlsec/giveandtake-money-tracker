from django.urls import path
from .views import *
from . import views

app_name = "customer"

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    
    path('delete_task/<str:pk>/', views.deleteTask, name="delete_task"),

    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name="register"),

    path('about-us/', views.aboutDeveloper, name="about_us"),
    path('user-profile/', views.user_profile, name="user_profile"),

    path('test/', views.test, name="test"),
    path('update_form/<str:pk>/', views.editTask, name='update_form'),
    path('add', views.addTask, name='add_form'),

]