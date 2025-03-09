from django.contrib import admin
from .models import technical_specification,Product
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title']

class technicalSpecificationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product,ProductAdmin)
admin.site.register(technical_specification,technicalSpecificationAdmin)