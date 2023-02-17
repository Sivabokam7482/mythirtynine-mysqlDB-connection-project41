from django.db import models

# Create your models here.
class customer(models.Model):
    cid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    email=models.EmailField()
    area=models.CharField(max_length=100)
    description=models.TextField()

    def __str__(self) :
        return self.name