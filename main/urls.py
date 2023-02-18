from django.urls import path
from . import views

# urls.py 
urlpatterns=[
    path('',views.landing),
    path('<int:pk>/', views.post_detail),
    path('index/', views.index),
    path('aboutme/', views.aboutme),
    
    

]