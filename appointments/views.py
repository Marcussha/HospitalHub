from django.shortcuts import render, redirect
from appointments.forms import AppointmentForm
from appointments.models import Appointment
from ministration.models import Ministration
from doctors.models import Doctors
from datetime import time

# Create your views here.

from django.shortcuts import render, redirect
from .models import Appointment
from ministration.models import Ministration

def create(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        datebooking = request.POST.get('datebooking')
        note = request.POST.get('note')
        timebooking_hour = request.POST.get('timebooking_hour')
        timebooking_minute = request.POST.get('timebooking_minute')

        # Get the selected Ministration and Doctor instances using their primary keys
        serviceid_id = request.POST.get('serviceid')
        serviceid = Ministration.objects.get(minisid=serviceid_id)

        docid_id = request.POST.get('docid')
        docid = Doctors.objects.get(doctorid=docid_id)

        # Combine timebooking_hour and timebooking_minute into a valid time object
        timebooking = time(int(timebooking_hour), int(timebooking_minute))

        try:
            Appointment.objects.create(
                fullname=fullname,
                email=email,
                phone=phone,
                datebooking=datebooking,
                serviceid=serviceid,
                docid=docid,
                note=note,
                timebooking=timebooking
            )
            return redirect('/appointments')  # Redirect to the appointments page after successful save
        except:
            pass

    # Retrieve the related instances for rendering the dropdown
    services = Ministration.objects.all()
    doctors = Doctors.objects.all()

    return render(request, "appointments/create.html", {'services': services, 'doctors': doctors})



def index (request): 
    appointment = Appointment.objects.all()
    return render(request, "appointments/index.html",{'appointment': appointment})

def clear (request,id):
    appointment = Appointment.objects.get( appid =id)
    appointment.delete()
    return redirect('/appointments')  