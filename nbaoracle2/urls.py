from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('lakers/', views.lakers, name="lakers"),
    path('pelicans/', views.pelicans, name="pelicans"),
    path('hawks/', views.hawks, name="hawks"),
]
