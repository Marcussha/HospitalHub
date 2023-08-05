from django.shortcuts import render, redirect
from doctors.models import Doctors
from doctors.forms import DoctorsForm

# Create your views here.
def index(request):
    doctors = Doctors.objects.all()
    return render(request, "doctors/show.html", {'doctors': doctors})

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
    doctor = Doctors.objects.get(doctorid=id)
    return render(request, 'doctors/edit.html', {'doctor': doctor})
    
def update(request, id):
    doctor = Doctors.objects.get(doctorid=id)
    form = DoctorsForm(request.POST, instance = doctor)
    if form.is_valid():
        form.save()
        return redirect("/doctors")
    return render(request, 'doctors/edit.html', {'doctor':doctor})
    
def clear(request, id):
    doctor = Doctors.objects.get(doctorid=id)
    doctor.delete()
    return redirect("/doctors")        
