from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login/', views.Login_view),
    path('register/', views.Register_view),
    path('EditProfile/', views.EditProfile),
    path('<str:username>/', views.UserProfile),
]