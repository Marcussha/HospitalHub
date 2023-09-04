from django.shortcuts import render,redirect
from authrole.forms import UserGroupsForm
from authrole.models import AuthUserGroups

# Create your views here.
def index (request):
    authroles = AuthUserGroups.objects.all()
    return render(request, 'authrole/index.html',{'authroles': authroles})

def create(request):
    if request.method == "POST":
        form = UserGroupsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/authrole')
            except:
                pass
    else:
        form = UserGroupsForm()
        return render(request,'authrole/create.html',{'form':form})