from django.db import models

# Create your models here.
class Client(models.Model):
    fullname = models.CharField(db_column='Fullname', max_length=70)  
    email = models.CharField(db_column='Email', unique=True, max_length=70)  
    birthday = models.DateField(db_column='Birthday')  
    address = models.CharField(db_column='Address', max_length=70)  
    telephone = models.IntegerField(db_column='Telephone')  
    sex = models.CharField(db_column='Sex', max_length=45) 

    class Meta:
        managed = False
        db_table = 'client'

    def __str__(self):
        return self.fullname