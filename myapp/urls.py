from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('hello/', views.hello),
    path('index/', views.index),
    path('show2/', views.show),
    path('showtiime/', views.showtiime),
    path('modelform/', views.modelform),
    path('djangoform/', views.djangoform),
    path('formvalidation/', views.employee),
    path('fileupload/', views.fileupload),
    path('getdata/', views.getdata),
    path('ssession/', views.setsession),
    path('gsession/', views.getsession),
    path('setcookie/', views.setcookie),
    path('getcookie/', views.getcookie),
    path('csv/', views.csv),
    path('redirect/', views.redirect_view),
]