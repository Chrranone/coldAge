from django.contrib import admin
from .models import Produce,ProduceType,ProgrameType,ProduceTypeTwo

@admin.register(ProduceType)
class ProduceTypeAdmin(admin.ModelAdmin):
    list_display = ('id','type_name')

@admin.register(ProduceTypeTwo)
class ProduceTypeTwoAdmin(admin.ModelAdmin):
    list_display = ('id','type_name')

@admin.register(Produce)
class ProduceAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','content','image','produce_type','information','information_image')

@admin.register(ProgrameType)
class ProgrameTypeAdmin(admin.ModelAdmin):
    list_display = ('id','type_name')

