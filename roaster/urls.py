"""
URL configuration for roaster app
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_resume, name='upload_resume'),
    path('results/<int:roast_id>/', views.results, name='results'),
    path('roast-again/<int:roast_id>/', views.roast_again, name='roast_again'),
    path('upvote/<int:roast_id>/', views.upvote, name='upvote'),
    # path('leaderboard/', views.leaderboard, name='leaderboard'),  # Disabled
]
