from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods
from django.template import loader
from myapp.form import *
from myapp.functions.functions import handle_uploaded_file  

# Create your views here.


@require_http_methods(["GET"])
def hello(request):
    return HttpResponse('<h1>This is Http GET request.</h1>')


def index(request):

    template = loader.get_template('index.html')
    name = {
        'student': 'Mohammad',
        'degree': 'Master'
    }
    return HttpResponse(template.render(name))


def show(request):
    now = datetime.datetime.now()
    html = '<html><body><h3>Now time is %s.</h3></body></html>' % now
    return HttpResponse(html)


def showtiime(request):
    template = loader.get_template('index.html')
    now = {
        'clock':  datetime.datetime.now()
    }
    return HttpResponse(template.render(now))


def modelform(request):
    student = EmpForm()
    return render(request, 'index.html', {'form': student})

# Django FORM
def djangoform(request):
    student = StudentForm()
    return render(request, 'index.html', {'form': student})


# Note: This function is for form validation
def employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                return redirect('/')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, 'index.html', {'form': form})

# Note: Check File upload
def fileupload(request):
    if request.method == 'POST':
        student = StudentForm(request.POST, request.FILES)
        if student.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("File uploaded successfuly")
    else:
        student = StudentForm()
        return render(request,"index.html",{'form':student})

