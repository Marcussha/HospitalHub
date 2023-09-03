from django.shortcuts import render, redirect
from doctors.models import Doctors 
from departments.models import Departments
from django.core.files.storage import FileSystemStorage
import os 

# Create your views here.
def index(request):
    doctor = Doctors.objects.all()
    return render(request, "doctors/show.html", {'doctor': doctor})

def create(request):
    if request.method == "POST":
        doctorname = request.POST.get('doctorname')
        email = request.POST.get('email')
        position = request.POST.get('position')
        note = request.POST.get('note')
        images = request.FILES.get('images')
        
        # Get the selected Department and Doctor instances using their primary keys
        departmentid_id = request.POST.get('departmentid')
        departmentid = Departments.objects.get(departmentid = departmentid_id )
        
    
        try:
            fs = FileSystemStorage()
            filename = fs.save(images.name, images)
            
            images_path = os.path.join('media', filename)
            Doctors.objects.create (
                    doctorname = doctorname,
                    email = email,
                    position = position,
                    note = note,
                    images = images_path,
                    departmentid = departmentid  
                )
            
            return redirect('/doctors')
        except Exception as e:
                print(str(e))
            
    departments = Departments.objects.all()
    return render(request,'doctors/index.html',{'departments': departments})
    
    
    
def edit(request,id):
    doctors = Doctors.objects.get(doctorid=id)
    return render(request, 'doctors/edit.html', {'doctors': doctors})
    
    
def clear(request, id):
    doctors = Doctors.objects.get(doctorid=id)
    
    if doctors.appointment_count > 0 or doctors.prescriptions_count > 0:
        error_message = "Cannot delete a doctors."
        return render (request, "error_page.html", {'error_message': error_message})
    
    doctors.delete()
    return redirect('/doctors')      

