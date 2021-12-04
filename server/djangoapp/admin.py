from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 1
# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name','maker')
# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_filter = ['name']
    list_display = ('name','description')
    search_fields = ['name']
# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)