
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('1/<int:my_id>/', views.valid, name = 'detail'),
]

 

