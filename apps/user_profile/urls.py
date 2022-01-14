from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="profile-index"),
    path("edit/<str:user>", views.edit, name="profile-edit"),
    path("degrees", views.degrees, name="degrees"),
]
