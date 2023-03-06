from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods
from django.template import loader
from myapp.form import StudentForm
from myapp.form import EmployeeForm
from myapp.form import EmpForm
from myapp.form import Employee
from myapp.functions.functions import handle_uploaded_file  
from django.core.exceptions import ObjectDoesNotExist
import csv
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

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

# Note: Exception Test
def getdata(request):  
    try:  
        data = Employee.objects.get(eid="12")  
    except ObjectDoesNotExist:  
        return HttpResponse("Exception: Data not found")  
    return HttpResponse(data)

# Note: Session Test
def setsession(request):
    request.session['sname'] = 'Mohammad'
    request.session['semail'] = 'mohammad@gmail.com'
    return HttpResponse('Session is set!')

def getsession(request):
    studentname = request.session['sname']
    studentemail = request.session['semail']
    return HttpResponse(studentname+ " " +studentemail)

# Note: Cookie Test
def setcookie(request):
    response = HttpResponse("Cookie Set!")
    response.set_cookie('MohammadCookie' , 'MohammadCookie2')
    return response

def getcookie(request):
    cookieTest = request.COOKIES['MohammadCookie']
    return HttpResponse('The cookie is: ' + cookieTest)

# Note: CSV Files Test
def csv(request):
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attachment; filename="file.csv"'
    writer = csv.writer(response)
    writer.writerow(['1001', 'John', 'Domil', 'CA'])
    writer.writerow(['1002', 'Amit', 'Mukharji', 'LA', '"Testing"'])
    return response

# User creation form
def register(request):  
    if request.POST == 'POST':  
        form = UserCreationForm()  
        if form.is_valid():  
            form.save()  
        messages.success(request, 'Account created successfully')
    else:
        form = UserCreationForm()  
        context = {  
            'form':form  
        }  
        return render(request, 'register.html', context)  