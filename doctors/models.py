from django.db import models
from django.db.models.query import QuerySet
from departments.models import Departments

# Create your models here.
class DoctorsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

class Doctors(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=70)
    position = models.CharField(max_length=50, blank=True, null=True)
    department = models.ForeignKey(Departments, models.DO_NOTHING, db_column='department')
    images = models.CharField(db_column='Images', max_length=255, blank=True, null=True)
    note = models.CharField(max_length=120, blank=True, null=True)

    objects = DoctorsManager()

    class Meta:
        managed = False
        db_table = 'doctors'

    def __str__(self):
        return self.name
    
    def get_queryset(self):
        return super().get_queryset().annotate(
            appointment_count=models.Count('appointment'),
            prescriptions_count=models.Count('prescriptions')
        )
    
    def delete(self, *args, **kwargs):
        if self.appointment_count > 0:
            raise ValueError("Cannot delete a doctor with associated appointments.")
        super().delete(*args, **kwargs)
