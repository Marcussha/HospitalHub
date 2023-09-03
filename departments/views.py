from django.shortcuts import render, redirect 
from departments.models import Departments
from departments.forms import DepartmentsForm

def index(request):
    # Retrieve the list of departments
    departments = Departments.objects.all()

    # Check if the user is an admin
    is_doctor = request.user.is_doctor

    # Pass the departments and is_admin variable to the template
    return render(request, "departments/show.html", {'departments': departments, 'is_staff': is_doctor})


def addnew(request):
    is_admin = request.user.is_admin
    if request.method == "POST":
        form = DepartmentsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/departments')
            except:
                pass
    else:
        form = DepartmentsForm()
        return render(request,'departments/index.html',{'form':form, 'is_admin':is_admin})
    
def edit(request,id):
    departments = Departments.objects.get(departmentid=id)
    return render(request, 'departments/edit.html', {'departments': departments})


def update(request, id):
    departments = Departments.objects.get(departmentid=id)
    form = DepartmentsForm(request.POST, instance = departments)
    if form.is_valid():
        form.save()
        return redirect("/departments")
    return render(request, 'departments/edit.html', {'departments':departments})


def clear(request, id):
    departments = Departments.objects.get(departmentid=id)
    
    if departments.doctors_count > 0:
        error_message = "Cannot delete a departments with associated doctor."
        return render(request, "error_page.html", {'error_message': error_message})
    
    departments.delete()
    return redirect("/departments")

