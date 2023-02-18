from django.urls import path
from . import views

# urls.py 
urlpatterns=[
    path('<int:pk>/', views.post_detail),
    path('', views.index),
    
    

]