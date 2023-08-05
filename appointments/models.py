from django.db import models
from django.contrib.auth.models import User as AuthUser
from ministration.models import Ministration
from doctors.models import Doctors

# Create your models here.

class Appointment(models.Model):
    appointmentid = models.AutoField(db_column='appointmentID', primary_key=True)  # Field name made lowercase.
    datebooking = models.DateTimeField(db_column='Datebooking')  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey(AuthUser, on_delete=models.DO_NOTHING, db_column='CustomerID', blank=True, null=True)
    serviceid = models.ForeignKey(Ministration, on_delete=models.DO_NOTHING, db_column='ServiceID', blank=True, null=True)  
    docid = models.ForeignKey(Doctors, on_delete=models.DO_NOTHING, db_column='DocID', blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'appointment'