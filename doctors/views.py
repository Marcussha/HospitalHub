from django.shortcuts import render, redirect
from doctors.models import Doctors 
from departments.models import Departments
from django.core.files.storage import FileSystemStorage
import os 

# Create your views here.

def home(request):
    doc = Doctors.objects.all()
    return render(request, "doctors/show.html", {'doc': doc})

def index(request):
    doctor = Doctors.objects.all()
    return render(request, "doctors/index.html", {'doctor': doctor})

def create(request):
    if request.method == "POST":
        doctorname = request.POST.get('doctorname')
        email = request.POST.get('email')
        position = request.POST.get('position')
        note = request.POST.get('note')
        images = request.FILES.get('images')
        
        # Get the selected Department and Doctor instances using their primary keys
        departmentid_id = request.POST.get('departmentid')
        departmentid = Departments.objects.get(departmentid=departmentid_id)
    
        try:
            fs = FileSystemStorage()
            filename = fs.save(images.name, images)
            
            # Store only the filename in the database, not the full path
            Doctors.objects.create(
                doctorname=doctorname,
                email=email,
                position=position,
                note=note,
                images=filename,  # Store the filename here
                departmentid=departmentid
            )
            
            return redirect('/doctors/index')
        except Exception as e:
            print(str(e))
            
    departments = Departments.objects.all()
    return render(request, 'doctors/create.html', {'departments': departments})
    
def edit(request,id):
    doctors = Doctors.objects.get(doctorid=id)
    return render(request, 'doctors/edit.html', {'doctors': doctors})
    
    
def clear(request, id):
    doctor = Doctors.objects.get(doctorid=id)
    
    if doctor.appointment_count > 0 or doctor.prescriptions_count > 0:
        error_message = "Cannot delete a doctors."
        return render (request, "error_page.html", {'error_message': error_message})
    
    doctor.delete()
    return redirect('/doctors/index')      

