from django.shortcuts import render,redirect
from authrole.forms import UserGroupsForm
from authrole.models import AuthUserGroups
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test
from authrole.custom_context import user_is_admin


# Create your views here.
@user_passes_test(lambda u: user_is_admin(u), login_url='login')
def index (request):
    authroles = AuthUserGroups.objects.all()
    return render(request, 'admin/authrole/index.html',{'authroles': authroles})

@user_passes_test(lambda u: user_is_admin(u), login_url='login')
def create(request):
    if request.method == "POST":
        # If the request method is POST, it means the form is submitted        
        form = UserGroupsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/authrole')# Redirect to the appropriate URL after successful creation
            except:
                return HttpResponse("An error occurred during user group creation.") 
    else:
        # If the request method is not POST, it means the user is accessing the page to fill out the form
        form = UserGroupsForm()
        return render(request,'admin/authrole/create.html',{'form':form})

@user_passes_test(lambda u: user_is_admin(u), login_url='login')
def delete(request, id):
    authroles = AuthUserGroups.objects.get(id=id)
    authroles.delete()
    return redirect('/authrole')