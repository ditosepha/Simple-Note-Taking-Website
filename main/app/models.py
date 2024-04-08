from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=2000)
    data_created = models.DateField()

    class Meta:
        db_table = "NOTE DATA"