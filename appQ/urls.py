from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile', views.profile, name='profile'),
    path('logout', views.logoutUser, name='logout'),
    path('test/<str:topic>', views.test, name='test'),

]