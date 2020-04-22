from django.http import HttpResponse
from django.shortcuts import render , redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


def Home(request,v1):
    return HttpResponse("welcome to python class {}".format(str(v1)))

def Home2(request):
    d={
        'S1':' Fesal','S2':'Munna','S3':'Prateek'
    }
    return render(request,"name.html",d)

def Home3(request):
    Students = ['Fesal','Munna','Prateek','Abhishek','Adarsh','Rohit']
    d = {
        "students":Students
    }
    return render(request,"places.html",d)

def Home4(request):
    students = ['Arjun','Vishal','Sachin','Rekhraj','Rahul']
    d={
        "Students":students
    }
    return render(request,"advantages.html",d)

def Home5(request):
    return render(request,"disadvantage.html")

def Home6(request):
    data = ["<center style='color:brown;'>core python","advance python and django","machine learning","IOT","Etc..</center>"]
    data = ", <br>".join(data)
    print (data)
    return HttpResponse (data)
def Home7(request):
    return HttpResponse("<center style='color:blue;'>my name is abhishek shukla" )
def Home8(request):
    return HttpResponse("<center style='color:blue;'>my name is abhishek shukla have to create plane")
def Home9(request):
    data = List.objects.all()
    Student = Students.objects.all()
    d={'Students':Student}
    d= {
        'List': data
    }
    return render(request,"index.html",d)

def Home10(request):
    Student = Students.objects.all()
    for s in Student:
        print(s.Name)
    b = {
        'students': Student
    }
    return render(request,'Students.html',b)

def Home13(request,v1):
    Liste=List.objects.filter(id = v1)
    F={'List':Liste}
    return render(request,'List.html',F)

def Home14(request,v3):
    return HttpResponse("python was learn ...{}".format(str(v3)))

def Home15(request,v4):
    sub = Subject.objects.all()
    s = {'sub':Subject}
    return render(request,'Subject.html',s)

def Detail(request,var):
    data = Students.objects.filter(id = var)
    d = {
        'Student': data
    }
    return render(request,"Details.html",d)

def Add_Number(request):
    if request.method =="POST":
        Value1=request.POST["a1"]
        Value2=request.POST["a2"]
        Total= int(Value1) +  int(Value2)
        return HttpResponse("<center>Addition is " + str(Total) +"</center>")
    return render(request,"Add_Number.html")

def Add_Students(request):
    institutes= institute.objects.all()
    if request.method =="POST":
        Nameins=request.POST["office"]
        Name=request.POST["name"]
        Email=request.POST["email"]
        Address=request.POST["address"]
        Mobile=request.POST["Moblie"]
        company=institute.objects.get(id=Nameins)
        Students.objects.create(Nameins=company,Name = Name,Number =Mobile,Email =Email,Address =Address)
        return  redirect(Home10)
    return render(request,"Add_student.html")

def Edit_Student(request,s_id,what):
    stu= Students.objects.get(id=s_id)
    if what=="Delete":
        stu.delete()
        return redirect()
    if request.method =="POST":
        Name= request.POST["name"]
        Email= request.POST["email"]
        Address= request.POST["address"]
        Mobile= request.POST["Moblie"]
        stu.Name = Name
        stu.Number =Mobile
        stu.Email =Email
        stu.Address =Address
        stu.save()
        return  redirect(Home10)
    d={"data":stu}
    return render(request,"Edit_student.html",d)

def institute(request):
    body=institute.objects.all()
    d={"institute":body}

    return render(request,"institute.html",d)



def login1(request):
    if request.method == "POST" :
        usr = request.POST["un"]
        ps = request.POST["ps"]
        Usr135 = authenticate(username = usr,password=ps)
        if Usr135:
            return HttpResponse("you logged In")
    return render(request,"login.html")

