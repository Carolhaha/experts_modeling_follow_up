from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import os
import sys
from django.shortcuts import render
import json


@csrf_exempt
def check(request):

    print("Go in")
    if request.is_ajax():
        if request.method == 'POST':
            output_string = request.body
            my_json = output_string.decode('utf8')
            data = json.loads(my_json)
            print(type(data))
            Outputfile(data)


    return HttpResponse("OK")

    request.encoding='utf-8'

def Outputfile(data):
    output_path = "templates/"+ data['path']
    print (data['fileid'])
    f = open(output_path,"w")
    f.write(data['fileid'])
    f.close()
    return
