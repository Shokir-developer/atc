from django.urls import path
from .views import *

urlpatterns = [

	path('', index, name='index'),
	path('lasts/', last30, name='last30'),

   
]