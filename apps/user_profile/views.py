from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.models import User
from apps.user_profile.forms import EditProfileForm
from apps.user_profile.models import Profile


# Create your views here.


@login_required
def index(req: request.HttpRequest):
    context = {"message": []}
    return render(req, "profile.html", context)


@login_required
def edit(req: request.HttpRequest, user: str):
    context = {"message": []}
    requested_user = User.objects.get(username__exact=user)
    if requested_user == req.user or req.user.is_staff == True:
        if req.method == "POST":
            try:
                # profile exists
                form = EditProfileForm(req.POST, instance=requested_user.profile)
                if form.is_valid():
                    form.save()
                    context["message"].append("Profile successfully updated")
            except Profile.DoesNotExist:
                new_profile = Profile.objects.get_or_create(
                    user=requested_user,
                )  # TODO: fill out rest of these fields

                form = EditProfileForm(req.POST, new_profile)
                context["message"].append("Profile successfully created")
        elif req.method == "GET":
            try:
                context["form"] = EditProfileForm(instance=requested_user.profile)
            except Profile.DoesNotExist:
                context["form"] = EditProfileForm()
    else:
        context["message"].append("permission denied")
    context["requested_user"] = requested_user
    context["error"] = context["form"].errors
    # TODO: don't forget about form.error checking as well
    return render(req, "edit.html", context)
