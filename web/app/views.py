from django.shortcuts import render

from django.http import Http404

from django.http import HttpResponse, JsonResponse
from .exceptions import InvalidArgs

# Create your views here.
def add(req):
    a = req.GET.get("a", "")
    b = req.GET.get("b", "")
    if not a or not b:
        raise InvalidArgs("Missing required args", 400)


    return JsonResponse(dict(sum=int(a)+int(b)))
