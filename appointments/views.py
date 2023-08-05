from django.shortcuts import render, redirect
from appointments.forms import AppointmentForm
from appointments.models import Appointment

# Create your views here.

def create (request):
    if request.method == "POST":  
        form = AppointmentForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/appointments')  
            except:  
                pass
    else:  
        form = AppointmentForm()
    return render(request,"appointments/create.html",{'form': form})


def index (request): 
    appointment = Appointment.objects.all()
    return render(request, "appointments/index.html",{'appointment': appointment})

def clear (request,id):
    appointment = Appointment.objects.get( appointmentid =id)
    appointment.delete()
    return redirect('/appointments')  