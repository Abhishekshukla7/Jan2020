"""Jan2020 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from MyApp.views import *

urlpatterns = [
    path('', admin.site.urls),
    path('name/<int:v1>/<int:v2>',Home),
    path('Abhishekshukla7.github.io/Jan2020/Definition/',Home2),
    path('Places/',Home3),
    path('Advantages/',Home4),
    path('Disadvantages/',Home5),
    path('courses/',Home6),
    path('intro/',Home7),
    path('motivation/',Home8),
    path('index/',Home9),
    path('Students/',Home10,name='sub'),
    path('List/<int:v1>/',Home13,name= 'List'),
    path('item/<int:v3>',Home14,name='ite'),
    path('Subject/<int:v4>/',Home15,name='ject'),
    path('Details/<int:var>/',Detail,name='Detail'),
    path('AddNumber/',Add_Number,name ="sum"),
    path('AddStudents/',Add_Students,name ="addsum"),
    path('EditStudents/<int:s_id>/<str:what>/',Edit_Student,name ="update"),
    path('Institute/',institute,name="ins"),
    path('login/', login1, name='log'),
]+  static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
