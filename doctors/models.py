from django.db import models
from departments.models import Departments

# Create your models here.
class Doctors(models.Model):
    doctorid = models.AutoField(db_column='DoctorID', primary_key=True)  # Field name made lowercase.
    doctorname = models.CharField(db_column='DoctorName', max_length=50)  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=50)  # Field name made lowercase.
    position = models.CharField(db_column='Position', max_length=50)  # Field name made lowercase.
    departmentid = models.ForeignKey(Departments, models.DO_NOTHING, db_column='DepartmentID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'doctors'

    def __str__ (self) :
        return self.doctorname
