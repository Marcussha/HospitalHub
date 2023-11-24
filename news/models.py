from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=45)
    content = models.CharField(max_length=500)
    pub_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'article'

    def __str__(self):
        return self.title