from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from .cat_info import CAT


# Create your views here.
def cat_view(request: HttpRequest) -> HttpResponse:
    return render(request, "home.html", {"cats": CAT})


def cat_details_view(request: HttpRequest, catName: str) -> HttpResponse:
    return render(request, "cat_details.html", {"cat": CAT[catName]})
