from django.contrib import admin
from userauths.models import User, ProfileUser


class AdminProfileUser(admin.ModelAdmin):
    list_display = ['full_name', 'user', 'date']
    

class AdminUser(admin.ModelAdmin):
    list_display= ['email']


admin.site.register(User)
admin.site.register(ProfileUser, AdminProfileUser)