from django.contrib import admin
from .models import userLogin, FileUpload
# Register your models here.
admin.site.register(userLogin)
admin.site.register(FileUpload)
