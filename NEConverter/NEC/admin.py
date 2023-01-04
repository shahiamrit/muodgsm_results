from django.contrib import admin
from .models import userLogin, sname
# Register your models here.
class snameAdmin(admin.ModelAdmin):
    list_display = ('dept', 'person', 'phonenumber')
    list_filter = ('dept',)

admin.site.register(userLogin)
admin.site.register(sname, snameAdmin)