from django.shortcuts import render, redirect
from doctors.models import Doctors 
from departments.models import Departments
from django.core.files.storage import FileSystemStorage

# Create your views here.
def home(request):
    doctor = Doctors.objects.all()
    return render(request, "doctors/show.html", {'doctors': doctor})

def index(request):
    doctor = Doctors.objects.all()
    return render(request, "doctors/index.html", {'doctors': doctor})

from django.contrib import messages

def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        position = request.POST.get('position')
        note = request.POST.get('note')
        images = request.FILES.get('images')
        
        # Get the selected Department and Doctor instances using their primary keys
        department = request.POST.get('department')
        department_instance = Departments.objects.get(departmentid=department)
    
        try:
            fs = FileSystemStorage()
            filename = fs.save(images.name, images)
            
            new_doctor = Doctors.objects.create(
                name=name,
                email=email,
                position=position,
                note=note,
                images=filename,
                department=department_instance,
            )

            # Include the newly created doctor in the context
            context = {'departments': Departments.objects.all(), 'new_doctor': new_doctor}
            return render(request, 'doctors/create.html', context)

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

