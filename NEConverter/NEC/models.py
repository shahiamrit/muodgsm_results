from django.db import models
import shortuuid
# Create your models here.

class FileUpload(models.Model):
    doc = models.FileField(upload_to ='uploads')
    token = models.CharField(max_length=22, default=shortuuid.uuid)

class userLogin(models.Model):
    studentname = models.CharField(max_length=200, blank=True, null=True)
    batch = models.CharField(max_length=500, blank=True, null=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    credithour = models.CharField(max_length=100, blank=True, null=True)
    grade = models.CharField(max_length=100, blank=True, null=True, unique=True)
    gradevalu = models.CharField(max_length=300, blank=True, null=True)
    lcgpa = models.CharField(max_length=200, blank=True, null=True)
    semlettergrade = models.CharField(max_length=400, blank=True, null=True)
    remarks = models.CharField(max_length=200, blank=True, null=True)
    dob = models.CharField(max_length=100, blank=True, null=True)
    symb = models.CharField(max_length=100, blank=True, null=True)
    
    subject1 = models.CharField(max_length=200, blank=True, null=True)
    credithour1 = models.CharField(max_length=100, blank=True, null=True)
    grade1 = models.CharField(max_length=100, blank=True, null=True, unique=True)
    gradevalu1 = models.CharField(max_length=300, blank=True, null=True)
    semlettergrade1 = models.CharField(max_length=400, blank=True, null=True)
    remarks1 = models.CharField(max_length=200, blank=True, null=True)

    subject2 = models.CharField(max_length=200, blank=True, null=True)
    credithour2 = models.CharField(max_length=100, blank=True, null=True)
    grade2 = models.CharField(max_length=100, blank=True, null=True, unique=True)
    gradevalu2 = models.CharField(max_length=300, blank=True, null=True)
    semlettergrade2 = models.CharField(max_length=400, blank=True, null=True)
    remarks2 = models.CharField(max_length=200, blank=True, null=True)

    subject3 = models.CharField(max_length=200, blank=True, null=True)
    credithour3 = models.CharField(max_length=100, blank=True, null=True)
    grade3 = models.CharField(max_length=100, blank=True, null=True, unique=True)
    gradevalu3 = models.CharField(max_length=300, blank=True, null=True)
    semlettergrade3 = models.CharField(max_length=400, blank=True, null=True)
    remarks3 = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.studentname