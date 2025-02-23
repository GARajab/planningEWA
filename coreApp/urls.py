from django.urls import path
from . import views

urlpatterns = [
    path("", views.signin_view, name="signin"),
    path("signup/", views.signup_view, name="signup"),
    path("signout/", views.signout_view, name="signout"),
    path("home/", views.home, name="home"),
    path("dbstatus/", views.my_view, name="my_view"),
    path("dep24/", views.depot24, name="depot24"),
]
