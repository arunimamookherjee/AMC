from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponseRedirect
import sys, os
import json
from django.http import JsonResponse
from tempfile import *

import subprocess


# Create your views here.
from django.http import HttpResponse





def modify(request):
    title=request.GET['title']
    return HttpResponseRedirect("/projectboard/base.html#/about")


def index(request):
    title=request.GET['title']
    file_detail=request.GET['name2']
    type=request.GET['optradio']
    ##number=request.GET['number']
    number=2
    command="sudo python3 /home/sony/environments/amc5.0/amc/projectboard/amc_python.py "+title
    os.system(command)
    os.chdir("/root")
    file_loc = "test.tex"
    f = open(file_loc, "w+")
    f.write(file_detail)
    f.close()

    command3="sudo mv test.tex /root/Projects/"+title
    os.system(command3)

    if type=="amc":
            command2 = "sudo python3 /home/sony/environments/amc5.0/amc/projectboard/amc_prepareTextTest.py " + title+" "+"2"


    else:
        command2 = "sudo python3 /home/sony/environments/amc5.0/amc/projectboard/amc_prepareTest.py " + title


    os.system(command2)

    return HttpResponseRedirect("/projectboard/base.html#/project2")

def index2(request):
    os.system("pwd")
    title=request.GET['project_name']
    cmd1="sudo xdg-open /root/Projects/"+title +"/amc-compiled.pdf"

    os.system(cmd1)
    return HttpResponseRedirect("/projectboard/base.html#/project2")

def view(request):

    if request.method == 'GET':
        fruit = request.GET['fruit']

    return render(request, "projectboard/about.html", {'personal_detail':fruit})


def markit(request):
    os.system('ls')
    title=request.GET['file']
    command="sudo python /home/sony/environments/amc5.0/amc/projectboard/amc_analyzeCopies.py "+title
    os.system(command)
    return HttpResponseRedirect("/projectboard/base.html#/project2")

def markit2(request):
    title=request.GET['file']
   # command="sudo xdg-open /root/Projects/"+title+"/exports/"+title+".csv"
   # os.system(" sudo xdg-open /root/Projects/hello7.0/exports/hello7.0.csv")

    os.system("sudo python /root/Projects/intoJSON.py ")

    return HttpResponseRedirect("/projectboard/base.html#/project2")

def random(request):
    os.system('python pypy.py')
   # data = open('/').read()  # opens the json file and saves the raw contents
    #jsonData = json.dumps(data)  #


    with open('out.json', 'r') as f:
        data = json.load(f)

    return HttpResponse(data, content_type="application/json")

def create_post(request):
    if request.method == 'GET':
        with open('out.json', 'r') as f:
            data = json.load(f)
        return HttpResponse(
            json.dumps(data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


