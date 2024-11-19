from django.urls import path
from . import views

app_name = 'grant_auth'

urlpatterns=[
    path('login/', views.grant_login, name='login'),
    path('register/', views.register, name='register'),
    path('captcha', views.send_email_captcha, name='captcha'),
    path('logout/', views.grant_logout, name='logout'),
]