from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('blazers/', views.trailblazers, name="blazers"),
    path('bucks/', views.bucks, name="bucks"),
    path('bulls/', views.bulls, name="bulls"),
    path('cavaliers/', views.cavaliers, name="cavaliers"),
    path('celtics/', views.celtics, name="celtics"),
    path('clippers/', views.clippers, name="clippers"),
    path('nets/', views.nets, name="nets"),
    path('grizzlies/', views.grizzlies, name="grizz"),
    path('hornets/', views.hornets, name="hornets"),
    path('mavericks/', views.mavericks, name="mavs"),
    path('heat/', views.heat, name="heat"),
    path('knicks/', views.knicks, name="knicks"),
    path('nuggets/', views.nuggets, name="nuggets"),
    path('pistons/', views.pistons, name="pistons"),
    path('lakers/', views.lakers, name="lakers"),
    path('pelicans/', views.pelicans, name="pelicans"),
    path('hawks/', views.hawks, name="hawks"),
    path('rockets/', views.rockets, name="rockets"),
    path('sixers/', views.sixers, name="sixers"),
    path('spurs/', views.spurs, name="spurs"),
    path('twolves/', views.twolves, name="twolves"),
    path('warriors/', views.warriors, name="warriors"),
]
