from django.shortcuts import render, redirect
from django.core.mail import send_mail
from appointments.models import Appointment
from ministration.models import Ministration
from doctors.models import Doctors
from datetime import time


# Create your views here.
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
              # Send confirmation email
            subject = "Appointment Confirmation"
            message = f"Hello {fullname},\n\nYour appointment is confirmed for {datebooking} at {timebooking_hour}:{timebooking_minute}.\nService: {serviceid}\nDoctor: {docid}\n\nThank you for choosing us!"
            from_email = "thonghqgcs200763@fpt.edu.vn"
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

            return redirect('/appointments')  
        except Exception as e:
            print("Error:", str(e))

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