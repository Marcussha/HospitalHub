from django.shortcuts import render, redirect 
from prescriptions.models import Prescriptions
from prescriptions.forms import PrescriptionsForm

# Create your views here.
def index(request):
    prescription = Prescriptions.objects.all()
    return render(request,"prescriptions/index.html", {'prescription':prescription})

def addnew(request):
    if request.method =="POST":
        form = PrescriptionsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/prescriptions')
            except:
                pass
    else:
        form = PrescriptionsForm()
        return render(request, 'prescriptions/create.html', {'form':form})
    
def edit(request, id):
    prescriptions = Prescriptions.objects.get(prescriptionid=id)
    return render(request, 'prescriptions/edit.html', {'prescriptons': prescriptions})

def update(request, id):
    prescriptions = Prescriptions.objects.get(prescriptionid=id)
    form = PrescriptionsForm (request.POST, instance = prescriptions)
    if form.is_valid():
        form.save()
        return redirect("/prescriptions")
    return render(request, 'prescriptions/edit.html', {'prescriptions':prescriptions})

def delete(request, id):
    prescription = Prescriptions.objects.get(prescriptionid=id)
    prescription.delete()
    return redirect("/prescriptions")