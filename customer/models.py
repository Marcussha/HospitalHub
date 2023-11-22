from django.db import models

# Create your models here.
class Client(models.Model):
    fullname = models.CharField(db_column='Fullname', max_length=70)  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=70)  # Field name made lowercase.
    birthday = models.DateField(db_column='Birthday')  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=70)  # Field name made lowercase.
    telephone = models.IntegerField(db_column='Telephone')  # Field name made lowercase.
    sex = models.CharField(db_column='Sex', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'client'

    def __str__(self):
        return self.fullname