from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(req):
    return HttpResponse("Hello world. You're at the pubsite")


def login(req):
    context = {"login"}
    return render(req, "", context)
