from django.contrib import admin
from mydb.models import AccessRecord, Account, Topic
from mydb.models import UserProfileInfo
# Register your models here.

admin.site.register(AccessRecord)
admin.site.register(Account)
admin.site.register(Topic)
admin.site.register(UserProfileInfo)

