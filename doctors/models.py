from django.db import models
from django.db.models.query import QuerySet
from departments.models import Departments

# Create your models here.
class DoctorsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().annotate(appointment_count=models.Count('appointment'),
                                               prescriptions_count=models.Count('prescriptions'))
class Doctors(models.Model):
    doctorid = models.AutoField(db_column='DoctorID', primary_key=True)  # Field name made lowercase.
    doctorname = models.CharField(db_column='DoctorName', max_length=50)  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=50)  # Field name made lowercase.
    position = models.CharField(db_column='Position', max_length=50)  # Field name made lowercase.
    departmentid = models.ForeignKey(Departments, models.DO_NOTHING, db_column='DepartmentID', blank=True, null=True)
    images =  models.ImageField(upload_to='doctors/media', null=True, blank=True)  # Field name made lowercase.# Field name made lowercase.

    objects = DoctorsManager()
    class Meta:
        managed = False
        db_table = 'doctors'

    def __str__ (self) :
        return self.doctorname
    
    def delete(self, *args, **kwargs):
        if self.appointment_count > 0:
            raise ValueError("Cannot delete a doctors with associated.")
        super().delete(*args, **kwargs)

