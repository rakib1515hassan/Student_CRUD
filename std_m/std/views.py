import os

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student_info
from django.db.models import Q

# Create your views here.
def base(request):
    return render(request, "std/base.html", {})
def home(request):
    std= Student_info.objects.all()
    return render(request, "std/home.html", {'std': std})

def add_std(request):
    if request.method=="POST":
        # Retreive the user inputs
        roll = request.POST.get("roll")
        full_name = request.POST.get("full_name")
        image = request.FILES.get("image")
        department = request.POST.get("department")
        email = request.POST.get("email")
        address = request.POST.get("address")
        phone = request.POST.get("phone")

        # Create an object for models class
        #s = Student_info.objects.create_user(roll = roll, full_name = full_name, image = image, department = department, email = email, address = address,phone = phone)
        s = Student_info()  # Hear i can pass the value, but i create empty constructor.
        # Here i assign the table value
        s.roll = roll
        s.full_name = full_name
        s.image = image
        s.department = department
        s.email = email
        s.address = address
        s.phone = phone

        s.save()  # To save our all data into database
        return redirect("add_std")

    return render(request, "std/add_std.html", {})

def delete_std(request, id):
    s = Student_info.objects.get(id=id)
    s.delete()
    return redirect("/std/home")

def update_std(request, id):
    std = Student_info.objects.get(id=id)
    return render(request, "std/update_std.html", {'std': std})
    #return HttpResponse("Update Student Information")

def do_update_std(request, id):
    if request.method=="POST":
        roll = request.POST.get("roll")
        full_name = request.POST.get("full_name")
        image = request.FILES.get("image")
        department = request.POST.get("department")
        email = request.POST.get("email")
        address = request.POST.get("address")
        phone = request.POST.get("phone")

        std = Student_info.objects.get(id=id)

        if len(request.FILES)!=0:
            if len(std.image)>0:
                os.remove(std.image.path)
            std.image = image

        std.roll = roll
        std.full_name = full_name
        std.department = department
        std.email = email
        std.address = address
        std.phone = phone
        std.save()  # To save our all data into database
        return redirect("/std/home")

def search(request):
    if request.method == "POST":
        query=request.POST.get("search")
        if query:
            query_set =(Q(full_name__icontains = query))|(Q(roll__icontains = query))|(Q(department__icontains = query))
            std = Student_info.objects.filter(query_set).distinct()
        else:
            std = []
    return render(request, 'std/home.html', {"std":std})

