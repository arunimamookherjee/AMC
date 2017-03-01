from django.shortcuts import render_to_response

# Create your views here.
from django.shortcuts import render, HttpResponseRedirect
import sys, os
import json
from django.http import JsonResponse
from django.template import Context, Template
from tempfile import *
import subprocess


# Create your views here.
from django.http import HttpResponse

file_name=""
ftype=""
no=0



def modify(request):

    number=request.GET['number']
    text=request.GET['name2']

    print(ftype)
    command3 = ""
    command2=""
    file_loc = ""

    if (ftype == "latex"):
        file_loc = "test.tex"
        command3 = "sudo mv test.tex /root/Projects/" + file_name

    elif (ftype == "amc"):
        file_loc = "test.txt"
        command3 = "sudo mv test.txt /root/Projects/" + file_name

    f = open(file_loc, "w+")
    f.write(text)
    f.close()
    os.system(command3)

    if ftype == "amc":
        command2 = "sudo python3 /home/sony/environments/amc5.0/amc/projectboard/amc_prepareTextTest.py " +file_name + " " + number
    elif ftype=="latex":
        command2 = "sudo python3 /home/sony/environments/amc5.0/amc/projectboard/amc_prepareTest.py " + file_name+" "+number

    os.system(command2)

    return HttpResponseRedirect("/projectboard/base.html#/project2")

#######################################################################
 #generates the folder and the question paper
def index(request):
    title=request.GET['title']

    file_detail = request.GET['name2']
    type = request.GET['optradio']
    command3 = ""
    file_loc=""
    number = request.GET['no']

    global   file_name
    file_name=title
    print(file_name)

    global ftype
    ftype = type

    command="sudo python3 /home/sony/environments/amc5.0/amc/projectboard/amc_python.py "+title
    os.system(command)
    os.chdir("/root")
    if(type=="latex"):
        file_loc = "test.tex"
        command3 = "sudo mv test.tex /root/Projects/" + title

    elif(type=="amc"):
        file_loc="test.txt"
        command3 = "sudo mv test.txt /root/Projects/" + title



    f = open(file_loc, "w+")
    f.write(file_detail)
    f.close()


    os.system(command3)

    if type=="amc":
        command2 = "sudo python3 /home/sony/environments/amc5.0/amc/projectboard/amc_prepareTextTest.py " + title+" "+number
    else:
        command2 = "sudo python3 /home/sony/environments/amc5.0/amc/projectboard/amc_prepareTest.py " + title+" "+number


    os.system(command2)


    return HttpResponseRedirect("/projectboard/base.html#/project2")

#######################################################################

def index2(request):
    os.system("pwd")
    os.chdir("/root/Projects")
    os.system("pwd")
    global file_name
    title=file_name
    print(file_name)


    cmd1="sudo xdg-open /root/Projects/"+title +"/DOC-subject.pdf"
    print(file_name)

    os.system(cmd1)
    return HttpResponseRedirect("/projectboard/base.html#/project2")
#######################################################################
def view(request):
        data = {"name": "daredevil"}
        return render_to_response("projectboard/about.html", {'my_data':'arunima'})
        ##return HttpResponseRedirect("/projectboard/base.html#/about")
#######################################################################

def markit(request):
    os.system('ls')
    title=request.GET['file']
    command="sudo python /home/sony/environments/amc5.0/amc/projectboard/amc_analyzeCopies.py "+title
    os.system(command)
    return HttpResponseRedirect("/projectboard/base.html#/project2")
#######################################################################
def dash(request):
    global file_name
    file_name=request.GET['title']
    return HttpResponseRedirect("/projectboard/base.html#/project2")

#######################################################################

def markit2(request):
    title=request.GET['file']
   # command="sudo xdg-open /root/Projects/"+title+"/exports/"+title+".csv"
   # os.system(" sudo xdg-open /root/Projects/hello7.0/exports/hello7.0.csv")

    os.system("sudo python /root/Projects/intoJSON.py ")

    return HttpResponseRedirect("/projectboard/base.html#/project2")
#######################################################################


def create_post(request):
    os.system('sudo python /root/Projects/intoJSON.py')

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
#######################################################################
def scan(request):
    num=request.GET['num']
    global file_name, no
    title=file_name
    no=num
    print("************initiating amc_scans.py**************"+title+"******"+str(num)+"*****")

    command = "sudo python /home/sony/environments/amc5.0/amc/projectboard/amc_scans.py " + title +" "+str(num)
    os.system(command)
    return HttpResponseRedirect("/projectboard/base.html#/project2")

######################################################################
def checkMate(request):
    global file_name, ftype
    title = file_name
    type=ftype

    print("************initiating amc_check.py**************" + title + "******"+type+"*****")

    if type=="latex":
        command = "sudo python /home/sony/environments/amc5.0/amc/projectboard/amc_check.py " + title + " tex"
    elif type=="amc":
        command = "sudo python /home/sony/environments/amc5.0/amc/projectboard/amc_check.py " + title + " txt"

    os.system(command)


    return HttpResponseRedirect("/projectboard/base.html#/project2")

#######################################################################

def associate(request):
    global file_name, ftype, no
    title = file_name
    type = ftype
    num=no

    print("************initiating amc_associate.py**************" + title + "*********")
    if type == "latex":
            command = "sudo python /home/sony/environments/amc5.0/amc/projectboard/amc_associate.py " + title+" "+str(num)+ " tex"
    elif type =="amc":
        command = "sudo python /home/sony/environments/amc5.0/amc/projectboard/amc_associate.py " + title + " " + str(
            num) + " txt"


    os.system(command)

    return HttpResponseRedirect("/projectboard/base.html#/project2")

########################################################################

def show():
    global file_name
    title = file_name



    return HttpResponseRedirect("/projectboard/base.html#/project2")
