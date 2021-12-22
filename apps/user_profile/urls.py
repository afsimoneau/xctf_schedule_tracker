from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="profile-index"),
    path("edit/<str:user>", views.edit, name="profile-edit"),
    path("edit/<str:user>/submit", views.edit_submit, name="profile-edit-submit"),
    path("degrees", views.degrees, name="degrees"),
    path("degrees/submit", views.degrees_submit, name="degrees-submit"),
]
