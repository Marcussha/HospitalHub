from django.shortcuts import render, redirect
from role.forms import RoleForm
from role.models import Roles

# Create your views here.

def create (request):
    if request.method == "POST":  
        form = RoleForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/roles')  
            except:  
                pass
    else:  
        form = RoleForm()
    return render(request,"role/create.html",{'form': form})


def index (request): 
    roles = Roles.objects.all()
    return render(request, "role/index.html",{'roles': roles})

def edit (request, id):
    role = Roles.objects.get( roleid =id)
    return render(request, "role/edit.html", {'role': role})

def update(request, id):
    role = Roles.objects.get(roleid =id)
    form = RoleForm(request.POST, instance = role)
    if form.is_valid():
        form.save()
        return redirect("/roles")
    return render(request,'role/edit.html', {'roles':role})

def clear (request,id):
    role = Roles.objects.get( roleid =id)
    role.delete()
    return redirect('/roles')  