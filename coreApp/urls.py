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
    path("delete/<str:permit_id>/", views.delete_depot24, name="delete_depot24"),
    path("delete25/<str:permit_id>/", views.delete_depot25, name="delete_depot25"),
    path("update/<int:id>/", views.update_depot_case, name="update_depot_case"),
    path("update25/<int:id>/", views.update_depot_case25, name="update_depot_case25"),
]
