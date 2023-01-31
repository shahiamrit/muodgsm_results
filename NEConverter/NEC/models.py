from django.db import models
import shortuuid
# Create your models here.

class FileUpload(models.Model):
    doc = models.FileField(upload_to ='uploads')
    token = models.CharField(max_length=22, default=shortuuid.uuid)

class userLogin(models.Model):
    studentname = models.CharField(max_length=200, blank=True, null=True, unique=True)
    batch = models.CharField(max_length=500, blank=True, null=True, unique=False)
    subject = models.CharField(max_length=200, blank=True, null=False, unique=False)
    credithour = models.CharField(max_length=100, blank=True, null=True, unique=False)
    grade = models.CharField(max_length=100, blank=True, null=True, unique=False)
    gradevalu = models.CharField(max_length=300, blank=True, null=True, unique=False)
    lcgpa = models.CharField(max_length=200, blank=True, null=True, unique=False)
    semlettergrade = models.CharField(max_length=400, blank=True, null=True, unique=False)
    remarks = models.CharField(max_length=200, blank=True, null=True, unique=False)
    dob = models.CharField(max_length=100, blank=True, null=True, unique=False)
    symb = models.CharField(max_length=100, blank=True, null=True, unique=False)
    reg = models.CharField(max_length=100, blank=True, null=True)
    result = models.CharField(max_length=100, blank=True, null=True, unique=False)
    
    subject1 = models.CharField(max_length=200, blank=True, null=True, unique=False)
    credithour1 = models.CharField(max_length=100, blank=True, null=True, unique=False)
    grade1 = models.CharField(max_length=100, blank=True, null=True, unique=False)
    gradevalu1 = models.CharField(max_length=300, blank=True, null=True, unique=False)
    remarks1 = models.CharField(max_length=200, blank=True, null=True, unique=False)

    subject2 = models.CharField(max_length=200, blank=True, null=True, unique=False)
    credithour2 = models.CharField(max_length=100, blank=True, null=True, unique=False)
    grade2 = models.CharField(max_length=100, blank=True, null=True, unique=False)
    gradevalu2 = models.CharField(max_length=300, blank=True, null=True, unique=False)
    remarks2 = models.CharField(max_length=200, blank=True, null=True, unique=False)

    subject3 = models.CharField(max_length=200, blank=True, null=True, unique=False)
    credithour3 = models.CharField(max_length=100, blank=True, null=True, unique=False)
    grade3 = models.CharField(max_length=100, blank=True, null=True, unique=False)
    gradevalu3 = models.CharField(max_length=300, blank=True, null=True, unique=False)
    remarks3 = models.CharField(max_length=200, blank=True, null=True, unique=False)


    def __str__(self):
        return self.studentname