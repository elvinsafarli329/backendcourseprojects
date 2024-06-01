from django.urls import path
from .views import *

app_name = "account"

urlpatterns = [
    path("register/", register_page, name="register"),
    path("login/", login_page, name="login"),
    path("logout/", logout_page, name="logout"),
    path("contact/", contact_page, name="contact"),
    path('success/', success_view, name='success'),
]