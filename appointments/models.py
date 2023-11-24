from django.db import models
from django.contrib.auth.models import User as AuthUser
from ministration.models import Ministration
from doctors.models import Doctors

# Create your models here.
class Appointment(models.Model):
    appid = models.AutoField(db_column='AppID', primary_key=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='Fullname', max_length=70)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50)  # Field name made lowercase.
    phone = models.IntegerField(db_column='Phone')  # Field name made lowercase.
    datebooking = models.DateField(db_column='Datebooking')  # Field name made lowercase.
    serviceid = models.ForeignKey(Ministration, on_delete=models.DO_NOTHING, db_column='ServiceID')
    docid = models.ForeignKey(Doctors, on_delete=models.DO_NOTHING, db_column='DocID' ) 
    note = models.CharField(db_column='Note', max_length=100, blank=True, null=True)  # Field name made lowercase.
    timebooking = models.TimeField(db_column='Timebooking', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'appointment'