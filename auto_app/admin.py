from django.contrib import admin
from .models import *

class AutoTechCHarAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'model', 'color', 'power', 'vin', 'year', 'car_milage', 'date_create', 'date_update')

class AutoBrandAdmin(admin.ModelAdmin):
    list_display = ('name',)

class AutoModelAdmin(admin.ModelAdmin):
    list_display = ('name_model',)

class AutoCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('profile_name', 'phone', 'email', 'date_create', 'date_update')

admin.site.register(AutoCategory, AutoCategoryAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(AutoBrand, AutoBrandAdmin)
admin.site.register(AutoModel, AutoModelAdmin)
admin.site.register(AutoTechCHar, AutoTechCHarAdmin)
