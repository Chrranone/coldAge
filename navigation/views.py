from django.shortcuts import render
from produce.models import ProduceType,ProgrameType,ProduceTypeTwo
# Create your views here.

def get_type_navigation():
    produce_type = ProduceType.objects.all()
    return produce_type

def get_type_navigation_two():
    produce_type_two = ProduceTypeTwo.objects.all()
    return produce_type_two

def get_programe_navigation():
    programe_type = ProgrameType.objects.all()
    return programe_type

