from django.db import models
from django.contrib.auth.models import User as AuthUser
from ministration.models import Ministration
from doctors.models import Doctors


# Create your models here.
class Appointment(models.Model):
    appid = models.AutoField(db_column='AppID', primary_key=True) 
    fullname = models.CharField(db_column='Fullname', max_length=70)  
    email = models.CharField(db_column='Email', max_length=50)  
    phone = models.IntegerField(db_column='Phone')  
    datebooking = models.DateField(db_column='Datebooking') 
    serviceid = models.ForeignKey(Ministration, on_delete=models.DO_NOTHING, db_column='ServiceID')
    docid = models.ForeignKey(Doctors, on_delete=models.DO_NOTHING, db_column='DocID' ) 
    note = models.CharField(db_column='Note', max_length=100, blank=True, null=True)  
    timebooking = models.TimeField(db_column='Timebooking', blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'appointment'