from django.shortcuts import render,redirect
from medicine.models import Medicine
from django.contrib import messages
 


# Create your views here.
def index(request):
    medicine = Medicine.objects.all()
    return render(request,"medicine/index.html", {'medicine':medicine})

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

def edit(request,id):
    medicine = Medicine.objects.get(id=id)
    return render(request, 'medicine/edit.html', {'medicine': medicine})


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

            return redirect('/medicine')
        except Exception as e:
            messages.error(request, 'An error occurred while updating the medicine.')
            
    return render(request, 'medicine/edit.html', {'medicine':medicine})


def clear(request, id):
    medicine = Medicine.objects.get(id=id)
    
    medicine.delete()
    return redirect('/medicine')      
    
             
