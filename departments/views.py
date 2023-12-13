from django.shortcuts import render, redirect 
from departments.models import Departments
from departments.forms import DepartmentsForm
from django.contrib.auth.decorators import user_passes_test
from authrole.custom_context import user_is_admin

@user_passes_test(lambda u: user_is_admin(u), login_url='login')
def index(request):
    # Retrieve the list of departments
    departments = Departments.objects.all()
    return render(request, "admin/departments/show.html",{'departments': departments})

@user_passes_test(lambda u: user_is_admin(u), login_url='login')
def addnew(request):
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
        return render(request,'admin/departments/create.html',{'form':form})
    
@user_passes_test(lambda u: user_is_admin(u), login_url='login')    
def edit(request,id):
    departments = Departments.objects.get(departmentid=id)
    return render(request, 'admin/departments/edit.html', {'departments': departments})

@user_passes_test(lambda u: user_is_admin(u), login_url='login')
def update(request, id):
    departments = Departments.objects.get(departmentid=id)
    form = DepartmentsForm(request.POST, instance = departments)
    if form.is_valid():
        form.save()
        return redirect("/departments")
    return render(request, 'admin/departments/edit.html', {'departments':departments})

@user_passes_test(lambda u: user_is_admin(u), login_url='login')
def clear(request, id):
    departments = Departments.objects.get(departmentid=id)
    
    if departments.doctors_count > 0:
        error_message = "Cannot delete a departments with associated doctor."
        return render(request, "error_page.html", {'error_message': error_message})
    
    departments.delete()
    return redirect("/departments")

