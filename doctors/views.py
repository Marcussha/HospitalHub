from django.shortcuts import render, redirect
from doctors.models import Doctors 
from departments.models import Departments
from django.core.files.storage import FileSystemStorage
from django.db import IntegrityError
from django.contrib import messages



# Create your views here.
def home(request):
    doctor = Doctors.objects.all()
    return render(request, "doctors/show.html", {'doctors': doctor})

def index(request):
    doctor = Doctors.objects.all()
    return render(request, "doctors/index.html", {'doctors': doctor})

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
            return render(request, 'doctors/index.html', context)

        except IntegrityError as e:
            # Check if the error is related to a duplicate key
            if 'unique constraint' in str(e).lower() and 'email' in str(e).lower():
                messages.error(request, 'Email already exists. Please choose a different email.')
            else:
                # Handle other IntegrityError cases if needed
                messages.error(request, 'An error occurred during the creation of the doctor.')

    departments = Departments.objects.all()
    return render(request, 'doctors/create.html', {'departments': departments})

    
def edit(request,id):
    doctors = Doctors.objects.get(id=id)
    return render(request, 'doctors/edit.html', {'doctors': doctors})
    
    
def clear(request, id):
    doctor = Doctors.objects.get(id=id)
    
    if doctor.appointment_count > 0 or doctor.prescriptions_count > 0:
        error_message = "Cannot delete a doctors."
        return render (request, "error_page.html", {'error_message': error_message})
    
    doctor.delete()
    return redirect('/doctors/index')      

