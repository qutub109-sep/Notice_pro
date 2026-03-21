from django.db import models

# Create your models here.

class registers(models.Model):
    full_name=models.CharField(max_length=50)
    email=models.EmailField()
    course=models.CharField(max_length=50)
    password=models.CharField(max_length=14)

    def __str__(self):
        return self.full_name


class Notice(models.Model):
    title = models.CharField(max_length=255)
    expiry_date = models.DateField()
    description = models.TextField()
    notice_pdf = models.FileField(upload_to='notices/', blank=True, null=True)

    def __str__(self):
        return self.title