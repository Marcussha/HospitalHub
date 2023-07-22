from django.db import models


class Departments(models.Model):
    departmentid = models.IntegerField(db_column='DepartmentID', primary_key=True)  # Field name made lowercase.
    named = models.CharField(db_column='NameD', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'departments'
# Create your models here.
