from django.urls import path

from . import views

urlpatterns = [
    path('abc', views.index),
    path('xyz',views.index1),
    path('login',views.login),
    path('sign',views.signup),
    path('users',views.getAllUser),
    path('states',views.getStates),
    path('districts/<str:id>/',views.getDistricts),
    path('shorturl',views.shorturl),
]