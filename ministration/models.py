from django.db import models

# Create your models here.

class Ministration(models.Model):
    minisid = models.IntegerField(db_column='MinisID', primary_key=True)  # Field name made lowercase.
    name_ministration = models.CharField(db_column='Name_ministration', max_length=70)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ministration'