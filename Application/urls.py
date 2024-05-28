from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home),
    path('signup/', views.signup),
    path('login/', views.login),
]
