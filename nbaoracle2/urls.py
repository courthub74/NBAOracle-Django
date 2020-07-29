from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('bucks/', views.bucks, name="bucks"),
    path('celtics/', views.celtics, name="celtics"),
    path('nets/', views.nets, name="nets"),
    path('hornets/', views.hornets, name="hornets"),
    path('mavericks/', views.mavericks, name="mavs"),
    path('nuggets/', views.nuggets, name="nuggets"),
    path('lakers/', views.lakers, name="lakers"),
    path('pelicans/', views.pelicans, name="pelicans"),
    path('hawks/', views.hawks, name="hawks"),
]
