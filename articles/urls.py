from django.urls import path, include
from . import views


app_name = "articles"
urlpatterns = [
    path('', views.home, name="home"),
    path('right/', views.right, name="right"),
    path('left/', views.left, name="left"),
]