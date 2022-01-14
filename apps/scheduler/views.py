from django.shortcuts import render
from django.http import HttpResponse, request
from django.contrib.auth.decorators import permission_required, login_required


# Create your views here.


@login_required
def index(req: request.HttpRequest):
    context = {}
    return render(req, "schedule-index.html", context)


@login_required
def edit(req: request.HttpRequest, user: str):
    context = {"message": [], "error": []}
    return render(req, "schedule-edit.html", context)
