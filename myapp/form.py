from django import forms
from myapp.models import Student
from myapp.models import Employee


# MODEL FORM
class EmpForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"


# Django FORM and Upload File
class StudentForm(forms.Form):
    firstname = forms.CharField(max_length=50, label='Enter First Name: ')
    lastname = forms.CharField(max_length=100, label='Enter Last Name: ')
    email = forms.EmailField(label='Enter Email: ')
    file = forms.FileField() #for creating file input


# MODEL FORM
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
