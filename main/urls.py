from django.urls import path
from . import views

# urls.py 
urlpatterns=[
    path('',views.landing, name= "landing"),
    path('<int:pk>/', views.post_detail, name="detail"),
    path('index/', views.index, name="index"),
    path('aboutme/', views.aboutme, name="aboutme"),
    
    

]