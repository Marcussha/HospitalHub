from django.db import models
from django.contrib.auth.models import User as AuthUser
from doctors.models import Doctors

class Prescriptions(models.Model):
    prescriptionid = models.AutoField(db_column='PrescriptionID', primary_key=True)  # Field name made lowercase.
    name_diseaase = models.CharField(db_column='Name_diseaase', max_length=50)  # Field name made lowercase.
    symptoms = models.CharField(db_column='Symptoms', max_length=70, blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    medicine = models.CharField(db_column='Medicine', max_length=70)  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=100, blank=True, null=True)  # Field name made lowercase.
    re_examination_date = models.DateTimeField(db_column='Re-examination_date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    doctorid = models.ForeignKey(Doctors, models.DO_NOTHING, db_column='DoctorID')  # Field name made lowercase.
    userid = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='UserID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'prescriptions'
