from django.urls import path
from django.contrib.auth import views as auth_views
from authentication.views import LoginView

app_name='authentication'
urlpatterns=[
path('login',LoginView,name='login'),
path('logout',auth_views.LogoutView.as_view(),name='logout'),
# path('register',auth_views.RegistrationView.as_view(template_name='authentication/register.html'),name='register')
]