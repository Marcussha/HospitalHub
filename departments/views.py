from django.shortcuts import render, redirect 
from departments.models import Departments
from departments.forms import DepartmentsForm

def index(request):
    # Retrieve the list of departments
    departments = Departments.objects.all()
    return render(request, "departments/show.html",{'departments': departments})



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
        return render(request,'departments/index.html',{'form':form})
    
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

def departments_search(request):
    query = request.GET.get('q')
    if query:
        results = Departments.objects.filter(name__icontains=query)
    else:
        results = Departments.objects.all()
    return render(request, 'departments/show.html',  {'results': results}) 


def clear(request, id):
    departments = Departments.objects.get(departmentid=id)
    
    if departments.doctors_count > 0:
        error_message = "Cannot delete a departments with associated doctor."
        return render(request, "error_page.html", {'error_message': error_message})
    
    departments.delete()
    return redirect("/departments")

