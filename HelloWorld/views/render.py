# -*- coding: utf-8 -*-

# This is the main entrance of the whole web interface.
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import resolve
from django.shortcuts import render
from django.http import HttpResponse
import os

@csrf_exempt
def Main(request):
    print("Render")

    return render(request, 'haha.html', {})

@csrf_exempt
def json(request):

    filepath = request.path.split("/")
    path = "templates/" + filepath[2] + "/" + filepath[3]
    # path = os.getcwd()
    # path = os.path.dirname(path)
    # path = os.path.dirname(path)
    # path = os.path.join(path , "templates")
    # path = os.path.join(path, "lsa")
    # path = os.path.join(path, "lsa01.json")

    str = ""
    with open(path , 'rb') as fp:
        str = fp.read()

    return HttpResponse(str)