from unicodedata import name
from django.urls import path
from webapp import views

urlpatterns = [
    path('', views.home, name='home' ),
    # path('removepunc', views.removepunc, name='rempun'),
    # path('capitalizefirst', views.capitalizefirst, name='capfirst'),
    # path('newlineremove', views.newlineremove, name='newlineremove'),
    # path('spaceremove', views.spaceremove, name='spaceremove'),
    
    path('analyze/', views.analyze, name='analyze'),

]