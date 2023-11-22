from django.shortcuts import render, redirect 
from prescriptions.models import Prescriptions
from customer.models import Client
from doctors.models import Doctors
from medicine.models import Medicine
from django.contrib import messages


# Create your views here.
def index(request):
    prescription = Prescriptions.objects.all()
    return render(request,"prescriptions/index.html", {'prescription':prescription})


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


    
#def edit(request, id):
    #prescriptions = Prescriptions.objects.get(prescriptionid=id)
    #return render(request, 'prescriptions/edit.html', {'prescriptons': prescriptions})

#def update(request, id):
    #prescriptions = Prescriptions.objects.get(prescriptionid=id)
    #form = PrescriptionsForm (request.POST, instance = prescriptions)
   # if form.is_valid():
        #form.save()
        #return redirect("/prescriptions")
    #return render(request, 'prescriptions/edit.html', {'prescriptions':prescriptions})

def delete(request, id):
    prescription = Prescriptions.objects.get(id=id)
    prescription.delete()
    return redirect("/prescriptions")