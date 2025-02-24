from django.urls import path
from . import views

urlpatterns = [
    path("", views.signin_view, name="signin"),
    path("signup/", views.signup_view, name="signup"),
    path("signout/", views.signout_view, name="signout"),
    path("home/", views.home, name="home"),
    path("dep24/", views.depot24, name="depot24"),
    path("dep25/", views.depot25, name="depot25"),
    path("lr24/", views.lr24, name="lr24"),
    path("lr25/", views.lr25, name="lr25"),
    path("nc/", views.nc24, name="nc24"),
    path("delete/<str:permit_id>/", views.delete_permit, name="delete_permit"),
]
