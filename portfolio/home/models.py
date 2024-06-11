from django.db import models

# Create your models here.
class Contact(models.Model):
    fname=models.CharField(max_length=50)
    email=models.EmailField()
    link=models.URLField()
    sub=models.CharField(max_length=100)
    msg=models.TextField()
    def __str__(self):
        return self.fname
    