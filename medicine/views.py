from django.shortcuts import render,redirect
from medicine.models import Medicine
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from authrole.custom_context import user_is_admin, user_is_doctor

# Create your views here.
@user_passes_test(lambda u: user_is_admin(u) or user_is_doctor(u), login_url='login')
def index(request):
    medicine = Medicine.objects.all()
    return render(request,"medicine/index.html", {'medicine':medicine})

@user_passes_test(lambda u: user_is_admin(u) or user_is_doctor(u), login_url='login')
def create(request):
    medicine = Medicine.objects.all()
    if request.method == "POST":
        name = request.POST.get('name')
        active_ingredient = request.POST.get('active_ingredient')
        manufacturer = request.POST.get('manufacturer')
    
        try:
            Medicine.objects.create(
                name = name,
                active_ingredient = active_ingredient,
                manufacturer = manufacturer,
            )
            return redirect('/medicine')
        except Exception as e:
            messages.error(request, 'An error occurred while creating new medicine.')

    return render(request, "medicine/create.html", {'medicine': medicine})

@user_passes_test(lambda u: user_is_admin(u) or user_is_doctor(u), login_url='login')
def edit(request,id):
    medicine = Medicine.objects.get(id=id)
    return render(request, 'medicine/edit.html', {'medicine': medicine})

@user_passes_test(lambda u: user_is_admin(u) or user_is_doctor(u), login_url='login')
def update(request, id):
    medicine = Medicine.objects.get(id=id)
    if request.method == 'POST':

        name = request.POST.get('name')
        active_ingredient = request.POST.get('active_ingredient')
        manufacturer = request.POST.get('manufacturer')

        try:
            medicine.name = name
            medicine.active_ingredient = active_ingredient
            medicine.manufacturer = manufacturer

            medicine.save()

            messages.success(request, 'Update successfully')

            return redirect('/medicine')
        except Exception as e:
            messages.error(request, 'An error occurred while updating the medicine.')
            
    return render(request, 'medicine/edit.html', {'medicine':medicine})

@user_passes_test(lambda u: user_is_admin(u) or user_is_doctor(u), login_url='login')
def clear(request, id):
    medicine = Medicine.objects.get(id=id)
    
    medicine.delete()
    return redirect('/medicine')      
    
             
