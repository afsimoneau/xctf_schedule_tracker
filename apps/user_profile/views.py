from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import permission_required, login_required
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.models import User
from apps.user_profile.forms import AddDegreeForm, EditProfileForm
from apps.user_profile.models import DegreeAndCert, Profile


# Create your views here.


@login_required
def index(req: request.HttpRequest):
    context = {"message": []}
    return render(req, "profile.html", context)


@login_required
@require_GET
def edit(req: request.HttpRequest, user: str):
    context = {"message": [], "error": []}
    requested_user = User.objects.get(username__exact=user)
    if requested_user == req.user or req.user.is_staff == True:
        try:
            context["form"] = EditProfileForm(instance=requested_user.profile)
        except Profile.DoesNotExist:
            context["error"].append("Profile doesn't exist")
            context["form"] = EditProfileForm()
    else:
        context["error"].append("permission denied")
    context["requested_user"] = requested_user
    # TODO: don't forget about form.error checking as well
    return render(req, "edit.html", context)


@login_required
@require_POST
def edit_submit(req: request.HttpRequest, user: str):
    context = {"message": [], "error": []}
    requested_user = User.objects.get(username__exact=user)
    if requested_user == req.user or req.user.is_staff == True:
        try:
            # profile exists
            form = EditProfileForm(data=req.POST, instance=requested_user.profile)
            if form.is_valid():
                form.save()
                context["message"].append("Profile successfully updated")
                context["form"] = form
            else:
                context["error"].append("Error saving form")
        except Profile.DoesNotExist:
            # no profile, do i need to pick a default degree?
            new_profile = Profile.objects.get_or_create(
                user=requested_user,
                event_group_1="DST",
                event_group_2="",
                year_in_school="FR",
            )
            form = EditProfileForm(data=req.POST, instance=new_profile)
            if form.is_valid():
                form.save()
                context["message"].append("Profile successfully created")
                context["form"] = form
    else:
        context["message"].append("permission denied")
    context["requested_user"] = requested_user
    # TODO: don't forget about form.error checking as well
    return render(req, "edit.html", context)


@login_required
@require_GET
def degrees(req: request.HttpRequest):
    context = {"message": [], "error": [], "degrees": {}}
    for level in DegreeAndCert.Levels:
        try:
            context["degrees"][level.value] = DegreeAndCert.objects.filter(
                level=level
            ).order_by("area_of_study")
        except DegreeAndCert.DoesNotExist:
            continue
    context["form"] = AddDegreeForm()
    print(context)
    return render(req, "degrees.html", context)


@login_required
@require_POST
def degrees_submit(req: request.HttpRequest):
    context = {"message": [], "error": [], "degrees": {}}

    form = AddDegreeForm(data=req.POST)
    if form.is_valid():
        form.save()
        context["message"].append("Added successfully")
        context["form"] = form
    else:
        context["error"].append("ERROR: not saved")
        context["form"] = form

    for level in DegreeAndCert.Levels:
        try:
            context["degrees"][level.value] = DegreeAndCert.objects.filter(
                level=level
            ).order_by("area_of_study")
        except DegreeAndCert.DoesNotExist:
            continue
    return render(req, "degrees.html", context)
