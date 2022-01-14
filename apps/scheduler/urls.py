from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="schedule-index"),
    path("edit/<str:user>", views.edit, name="schedule-edit"),
]
