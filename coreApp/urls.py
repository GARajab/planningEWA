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
    path("delete24/<str:permit_id>/", views.delete_depot24, name="delete_depot24"),
    path("deleteNc/<str:permit_id>/", views.delete_Nc, name="delete_Nc"),
    path("deleteLR24/<str:permit_id>/", views.delete_LR24, name="delete_LR24"),
    # path("deleteLR25/<str:permit_id>/", views.delete_LR25, name="delete_LR25"),
    path("delete25/<str:permit_id>/", views.delete_depot25, name="delete_depot25"),
    path("updateLR24/<int:id>/", views.update_LR24, name="update_LR24"),
    # path("updateLR25/<int:id>/", views.update_LR25, name="update_LR25"),
    path("update24/<int:id>/", views.update_depot24, name="update_depot24"),
    path("update25/<int:id>/", views.update_depot25, name="update_depot25"),
    path("updateNc/<int:permit_id>/", views.edit_permit, name="edit_permit"),
    path("dep24rep/", views.depot24Report, name="depot24Report"),
    path("lr24rep/", views.LR24Report, name="LR24Report"),
    path("dep25rep/", views.depot25Report, name="depot25Report"),
    path("lr25rep/", views.loadReading2024Report, name="loadReading2024Report"),
    path("view_dep24/<int:id>", views.view_case_dep_24, name="view_case_dep_24"),
    path("view_nc/<int:id>", views.view_case_nc, name="view_case_nc"),
    path("view_dep25/<int:id>", views.view_case_dep_25, name="view_case_dep_25"),
    path("LR/<int:id>/", views.loadreading_detail_view, name="loadreading_detail_view"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path(
        "fetch-scheme-references/<str:year>/",
        views.fetch_scheme_references,
        name="fetch_scheme_references",
    ),
    path(
        "fetch-scheme-references/",
        views.fetch_scheme_references,
        name="fetch_scheme_references",
    ),
]
