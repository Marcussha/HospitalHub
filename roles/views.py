from django.shortcuts import render, redirect
from roles.models import AuthGroup
from .forms import RoleForm
from django.contrib.auth.decorators import user_passes_test
from authrole.custom_context import user_is_admin

# Create your views here.
@user_passes_test(lambda u: user_is_admin(u), login_url='login')
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
    return render(request,"admin/role/create.html",{'form': form})

@user_passes_test(lambda u: user_is_admin(u), login_url='login')
def index (request): 
    roles = AuthGroup.objects.all()
    return render(request, "admin/role/index.html",{'roles': roles})

@user_passes_test(lambda u: user_is_admin(u), login_url='login')
def edit (request, id):
    role = AuthGroup.objects.get( id =id)
    return render(request, "admin/role/edit.html", {'role': role})

@user_passes_test(lambda u: user_is_admin(u), login_url='login')
def update(request, id):
    role = AuthGroup.objects.get(id =id)
    form = RoleForm(request.POST, instance = role)
    if form.is_valid():
        form.save()
        return redirect("/roles")
    return render(request,'admin/role/edit.html', {'roles':role})

@user_passes_test(lambda u: user_is_admin(u), login_url='login')
def clear(request, id):
    role = AuthGroup.objects.get( id =id)
    role.delete()
    return redirect('/roles')  

