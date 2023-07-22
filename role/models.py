from django.db import models

# Create your models here.
class Roles(models.Model):
    roleid = models.IntegerField(db_column='RoleID', primary_key=True)  # Field name made lowercase.
    rolename = models.CharField(db_column='RoleName', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'roles'