from django.shortcuts import render, redirect 
from prescriptions.models import Prescriptions
from customer.models import Client
from doctors.models import Doctors
from medicine.models import Medicine
from django.contrib import messages
from prescriptions.filters import PrescriptionFilter
from django.http import Http404
from django.db.utils import IntegrityError
from django.contrib.auth.decorators import user_passes_test
from authrole.custom_context import user_is_admin, user_is_doctor

# Create your views here
@user_passes_test(lambda u: user_is_admin(u) or user_is_doctor(u), login_url='login')
def index(request):
    prescription = Prescriptions.objects.all()
    prescriptionFilter = PrescriptionFilter(request.GET, queryset=prescription)
    prescription = prescriptionFilter.qs
    
    return render(request,"prescriptions/index.html", {'prescription':prescription, 'filter': PrescriptionFilter})


@user_passes_test(lambda u: user_is_admin(u) or user_is_doctor(u), login_url='login')
def create(request):
    prescription = Prescriptions.objects.all()
    
    doctor = Doctors.objects.all()
    medicines = Medicine.objects.all()
    patient = Client.objects.all()

    if request.method == "POST":
        name_disease = request.POST.get('name_disease')
        symptoms = request.POST.get('symptoms')
        start_date = request.POST.get('start_date')
        re_examination_date = request.POST.get('re_examination_date')
        note = request.POST.get('note')

        patient_id = request.POST.get('patient')  
        patient = Client.objects.get(id=patient_id)

        doctor_id = request.POST.get('doctor')

        try:
            doctor = Doctors.objects.get(id=doctor_id)
        except Doctors.DoesNotExist:
            messages.error(request, f'Doctor with ID {doctor_id} does not exist.')
            return redirect('/prescriptions')

        medicine_id = request.POST.get('medicine')  
        medicine = Medicine.objects.get(id=medicine_id)

        try:
            Prescriptions.objects.create(
                name_disease=name_disease,
                patient=patient,
                doctor=doctor,
                symptoms=symptoms,
                medicine=medicine,
                start_date=start_date,
                re_examination_date=re_examination_date,
                note=note,
                
            )
            print(f"Prescription created: {prescription}")
            return redirect('/prescriptions')
        except Exception as e:
            print(f"Error creating prescription: {e}")
            messages.error(request, 'An error occurred while creating new Prescriptions.')

    return render(request, 'prescriptions/create.html', {'prescription': prescription, 'doctors': doctor, 'medicines': medicines, 'patient': patient})


@user_passes_test(lambda u: user_is_admin(u) or user_is_doctor(u), login_url='login')    
def edit(request, id):
    prescription = Prescriptions.objects.get(id=id)

    #Retrieve all patients, doctors, and medicines for the form
    patients = Client.objects.all()
    doctors = Doctors.objects.all()
    medicines = Medicine.objects.all()
    
    return render(request, 'prescriptions/edit.html', {'prescription': prescription, 'patients': patients, 'doctors': doctors, 'medicines': medicines})


@user_passes_test(lambda u: user_is_admin(u) or user_is_doctor(u), login_url='login')
def update(request, id):
    try:
        prescription = Prescriptions.objects.get(id=id)

        if request.method == 'POST':
            name_disease = request.POST.get('name_disease')
            symptoms = request.POST.get('symptoms')
            start_date = request.POST.get('start_date')
            re_examination_date = request.POST.get('re_examination_date')
            note = request.POST.get('note')

            # Retrieve related instances using their primary keys
            patient_id = request.POST.get('patient')
            patient = Client.objects.get(id=patient_id)

            doctor_id = request.POST.get('doctor')

            try:
                doctor = Doctors.objects.get(id=doctor_id)
            except Doctors.DoesNotExist:
                messages.error(request, f'Doctor with ID {doctor_id} does not exist.')
                return redirect('/prescriptions')

            medicine_id = request.POST.get('medicine')
            medicine = Medicine.objects.get(id=medicine_id)

            # Update the prescription object with new data
            prescription.name_disease = name_disease
            prescription.patient = patient
            prescription.doctor = doctor
            prescription.symptoms = symptoms
            prescription.medicine = medicine
            prescription.start_date = start_date
            prescription.re_examination_date = re_examination_date
            prescription.note = note

            prescription.save()

            messages.success(request, 'Prescription updated successfully.')
            return redirect('/prescriptions')

    except Prescriptions.DoesNotExist:
        messages.error(request, f'Prescription with ID {id} does not exist.')

    return render(request, 'prescriptions/edit.html', {'prescription': prescription})


@user_passes_test(lambda u: user_is_admin(u) or user_is_doctor(u), login_url='login')
def delete(request, id):
    try:
        prescription = Prescriptions.objects.get(id=id)
        prescription.delete()
    except Prescriptions.DoesNotExist:
        raise Http404("Prescription does not exist")
    except IntegrityError as e:
        error_message = f"Cannot delete prescription: {e}"
        return render(request, "error_page.html", {'error_message': error_message})

    return redirect('/prescriptions')