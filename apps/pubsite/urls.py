from django.urls import path
from django.contrib.auth import views as auth_views


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", auth_views.LoginView.as_view(), name="pub-login"),
    path("logout", auth_views.LogoutView.as_view(), name="pub-logout"),
    path(
        "reset/confirm",
        auth_views.PasswordResetConfirmView.as_view(),
        name="reset-confirm",
    ),
    path(
        "reset/complete",
        auth_views.PasswordResetCompleteView.as_view(),
        name="reset-complete",
    ),
    path("reset/done", auth_views.PasswordResetDoneView.as_view(), name="reset-done"),
    path("reset", auth_views.PasswordResetView.as_view(), name="reset"),
]
