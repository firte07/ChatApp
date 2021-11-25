from django.urls import path, include
from . import views
from django.views.generic import RedirectView
from django.conf.urls import url

urlpatterns = [
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
    path('send', views.send, name='send'),
    path('', views.loginPage, name='login'),
    path('invite', views.invite, name='invite'),
    path('<str:room>/', views.room, name='room'),
    path('logout', views.logoutUser, name='logout'),
    path('register', views.registerPage, name='register'),
    path('enter/<str:username>/', views.home, name='home'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    path('enter/<str:username>/checkview', views.checkview, name='checkview'),
    path('getInvitations/<str:username>/', views.getInvitations, name='getInvitations')
]
