from django.shortcuts import render, redirect
from doctors.models import Doctors
from doctors.forms import DoctorsForm

# Create your views here.
def index(request):
    doctor = Doctors.objects.all()
    return render(request, "doctors/show.html", {'doctor': doctor})

def addnew(request):
    if request.method == "POST":
        form = DoctorsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/doctors')
            except:
                pass
    else:
        form = DoctorsForm()
        return render(request,'doctors/index.html',{'form':form})
    
def edit(request,id):
    doctors = Doctors.objects.get(doctorid=id)
    return render(request, 'doctors/edit.html', {'doctors': doctors})
    
def update(request, id):
    doctors = Doctors.objects.get(doctorid=id)
    form = DoctorsForm(request.POST, instance = doctors)
    if form.is_valid():
        form.save()
        return redirect("/doctors")
    return render(request, 'doctors/edit.html', {'doctors':doctors})
    
def clear(request, id):
    doctors = Doctors.objects.get(doctorid=id)
    
    if doctors.appointment_count > 0 or doctors.prescriptions_count > 0:
        error_message = "Cannot delete a doctors."
        return render (request, "error_page.html", {'error_message': error_message})
    
    doctors.delete()
    return redirect('/doctors')        
