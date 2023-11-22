from django.db import models

# Create your models here.
class Medicine(models.Model):
    name = models.CharField(max_length=255)
    active_ingredient = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medicine'

    def __str__(self):
        return self.name