from django.urls import path
from . import views

urlpatterns = [
    path("signin",views.signin),
    path("signup",views.signup),
    path("",views.home),
    path("logout_from_home",views.logout_from_home),
    path("register",views.register)
]