from django.shortcuts import render,redirect
from authrole.forms import UserGroupsForm
from authrole.models import AuthUserGroups
from django.http import HttpResponse
from django.contrib import messages
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
        form = UserGroupsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Assign role successfully.')
                return redirect('/authrole') 
            except Exception as e:
                messages.error(request, f'An error occurred during user group creation: {e}')
        else:
            messages.error(request, 'This username is already taken, please choose another one')
    else:
        form = UserGroupsForm()

    return render(request, 'admin/authrole/create.html', {'form': form})


@user_passes_test(lambda u: user_is_admin(u), login_url='login')
def delete(request, id):
    authroles = AuthUserGroups.objects.get(id=id)
    authroles.delete()
    return redirect('/authrole')