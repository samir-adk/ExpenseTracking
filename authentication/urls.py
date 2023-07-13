from django.urls import path
from django.contrib.auth import views as auth_views
from authentication.views import LoginView,RegisterView,LogoutView

app_name='authentication'
urlpatterns=[
path('login',LoginView,name='login'),
path('logout',LogoutView,name='logout'),
path('register',RegisterView,name='register')
]