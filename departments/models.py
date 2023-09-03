from django.db import models
from django.db.models.query import QuerySet

class DepartmentsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().annotate(doctors_count = models.Count('doctors'))
    
class Departments(models.Model):
    departmentid = models.AutoField(db_column='DepartmentID', primary_key=True)  # Field name made lowercase.
    named = models.CharField(db_column='NameD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    
    objects = DepartmentsManager()
    class Meta:
        managed = False
        db_table = 'departments'
        permissions = [
            ("can_manage_departments", "Can manage departments"),
        ]

    def __str__(self):
        return self.named
    
    def delete(self, *args, **kwargs):
        if self.doctors_count > 0:
            raise ValueError("Cannot delete a departments with associated doctor.")
        super().delete(*args, **kwargs)