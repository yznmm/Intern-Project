from django.urls import path
from . import views
 

urlpatterns =[
    path('', views.main, name='main'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('cat/', views.cat, name='cat'),
    path('dog/', views.dog, name='dog'),
    path('admincat/', views.admincat, name='admincat'),
    path('admindog/', views.admindog, name='admindog'), 
]
