from django.db import models
from customer.models import Client
from doctors.models import Doctors
from medicine.models import Medicine

class Prescriptions(models.Model):
    name_disease = models.CharField(max_length=200)
    patient = models.ForeignKey(Client, models.DO_NOTHING, db_column='patient')
    doctor = models.ForeignKey(Doctors, models.DO_NOTHING, db_column='doctor')
    symptoms = models.CharField(max_length=200, blank=True, null=True)
    medicine = models.ForeignKey(Medicine, models.DO_NOTHING, db_column='medicine')
    start_date = models.DateField(blank=True, null=True)
    re_examination_date = models.DateField(blank=True, null=True)
    note = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prescriptions'
