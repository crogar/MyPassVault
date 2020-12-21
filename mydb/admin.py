from django.contrib import admin
from mydb.models import AccessRecord, Account, Topic

# Register your models here.

admin.site.register(AccessRecord)
admin.site.register(Account)
admin.site.register(Topic)



