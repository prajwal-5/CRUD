from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistrationForm
from .models import Student

# Function to show the interface
def add_show(req):
    if req.method == "POST":
        fm = StudentRegistrationForm(req.POST)
        if fm.is_valid():
            nm = fm.cleaned_data["name"]
            em = fm.cleaned_data["email"]
            pa = fm.cleaned_data["password"]
            reg = Student(name=nm, email=em, password=pa)
            reg.save()
            fm=StudentRegistrationForm()
    else:
        fm = StudentRegistrationForm()

    stud = Student.objects.all()
    return render(req, "enroll/addandshow.html",{'form':fm, 'stu':stud})


# Function to update details
def update_data(req, id):
    if req.method=='POST':
        pi = Student.objects.get(pk=id)
        fm = StudentRegistrationForm(req.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Student.objects.get(pk=id)
        fm = StudentRegistrationForm(instance=pi)
    return render(req, "enroll/updatestudent.html", {'form': fm})


# Function to delete the record
def del_data(req, id):
    if req.method=="POST":
        pi = Student.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')