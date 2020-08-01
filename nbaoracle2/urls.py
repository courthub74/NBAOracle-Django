from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('blazers/', views.trailblazers, name="blazers"),
    path('bucks/', views.bucks, name="bucks"),
    path('bulls/', views.bulls, name="bulls"),
    path('celtics/', views.celtics, name="celtics"),
    path('clippers/', views.clippers, name="clippers"),
    path('nets/', views.nets, name="nets"),
    path('hornets/', views.hornets, name="hornets"),
    path('mavericks/', views.mavericks, name="mavs"),
    path('heat/', views.heat, name="heat"),
    path('nuggets/', views.nuggets, name="nuggets"),
    path('pistons/', views.pistons, name="pistons"),
    path('lakers/', views.lakers, name="lakers"),
    path('pelicans/', views.pelicans, name="pelicans"),
    path('hawks/', views.hawks, name="hawks"),
    path('rockets/', views.rockets, name="rockets"),
    path('warriors/', views.warriors, name="warriors"),
]
