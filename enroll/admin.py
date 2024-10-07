from django.contrib import admin

# Register your models here.
from .models import user

@admin.register(user) #decorator
class userAdmin(admin.ModelAdmin):
    list_display =('id','name','email','password','Rpassword')