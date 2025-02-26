from django.urls import path
from django.http import HttpResponse
from gsvtech_app.views import welcome, index, sobre, servicos, contato 

urlpatterns = [

    path('welcome/', welcome),
    path('', index),
    path('sobre/', sobre),
    path('servicos/', servicos),
    path('contato/', contato),
    
]