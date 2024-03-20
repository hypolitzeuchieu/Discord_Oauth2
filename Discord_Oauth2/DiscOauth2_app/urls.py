from django.urls import path
from .views import home, discord_login, discord_login_redirect

urlpatterns = [
    path('oauth2/', home, name='home'),
    path('login/', discord_login, name='discord_login'),
    path('oauth2/login/redirect', discord_login_redirect, name='discord_login_redirect'),
]
