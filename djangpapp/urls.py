"""djangpapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from myapp import urls
from employee import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('', include('employee.urls')), 
    # path('hello/', include(myappViews.hello)),
    # path('index/', include(myappViews.index)),
    # path('show/', include(myappViews.show)),
    # path('showtiime/', include(myappViews.showtiime)),
    # path('modelform/', include(myappViews.modelform)),
    # path('djangoform/', include(myappViews.djangoform)),
    # path('formvalidation/', include(myappViews.employee)),
    # path('fileupload/', include(myappViews.fileupload)),
    # path('getdata/', include(myappViews.getdata)),
    # path('ssession/', include(myappViews.setsession)),
    # path('gsession/', include(myappViews.getsession)),
    # path('setcookie/', include(myappViews.setcookie)),
    # path('getcookie/', include(myappViews.getcookie)),
    # path('csv/', include(myappViews.csv)),
    # path('emp', include(employeeViews.emp)),
    # path('show',include(employeeViews.show)),  
    # path('edit/<int:id>', include(employeeViews.edit)),  
    # path('update/<int:id>', include(employeeViews.update)),  
    # path('delete/<int:id>', include(employeeViews.destroy)),  
]
