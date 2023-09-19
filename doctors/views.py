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

def doctor_search(request):
    query = request.GET.get('q')
    if query:
        results = Doctors.objects.filter(name__icontains=query)
    else:
        results = Doctors.objects.all()
    return render(request, 'doctors/show.html',  {'results': results}) 

def update(request, id):
    try:
        doctors = Doctors.objects.get(doctorid=id)
    except Doctors.DoesNotExist:
        # Handle the case where the doctor with the given id doesn't exist
        return redirect('/doctors/index')  # You can redirect to a suitable page

    if request.method == "POST":
        try:
            doctorname = request.POST.get('doctorname')
            email = request.POST.get('email')
            position = request.POST.get('position')
            note = request.POST.get('note')
            images = request.FILES.get('images')
            
            if images:
                # If a new image is uploaded, update it
                fs = FileSystemStorage()
                filename = fs.save(images.name, images)
                doctors.images = filename

            # Update other fields
            doctors.doctorname = doctorname
            doctors.email = email
            doctors.position = position
            doctors.note = note
            doctors.save()  # Save the changes to the doctor object

            return redirect('/doctors/index')  # Redirect to the doctor list page after updating
        except Exception as e:
            print(str(e))
    
    return render(request, 'doctors/edit.html', {'doctors': doctors})


def clear(request, id):
    doctor = Doctors.objects.get(doctorid=id)
    
    if doctor.appointment_count > 0 or doctor.prescriptions_count > 0:
        error_message = "Cannot delete a doctors."
        return render (request, "error_page.html", {'error_message': error_message})
    
    doctor.delete()
    return redirect('/doctors/index')      

