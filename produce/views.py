from django.shortcuts import render,get_object_or_404
from .models import Produce,ProduceType,ProgrameType,ProduceTypeTwo
from navigation.views import get_type_navigation,get_programe_navigation,get_type_navigation_two
from blog.views import get_type_blog

# Create your views here.

def produce_list(request,produce_type_pk):
    produce_type = get_object_or_404(ProduceType,pk=produce_type_pk)
    produces_all_list = Produce.objects.filter(produce_type=produce_type)
    
    context = {}
    context['produces'] = produces_all_list

    context['produce_types'] = get_type_navigation()
    context['blog_types'] = get_type_blog()
    context['programe_types'] = get_programe_navigation()
    context['produce_types_two'] = get_type_navigation_two()
    return render(request,'produce_list.html',context)

def produce_list_two(request,produce_type_two_pk):
    produce_type_two = get_object_or_404(ProduceTypeTwo,pk=produce_type_two_pk)
    produces_all_list = Produce.objects.filter(produce_type_two=produce_type_two)
    
    context = {}
    context['produces'] = produces_all_list

    context['produce_types'] = get_type_navigation()
    context['blog_types'] = get_type_blog()
    context['programe_types'] = get_programe_navigation()
    context['produce_types_two'] = get_type_navigation_two()
    return render(request,'produce_list.html',context)

def programe(request,programe_pk):
    programe_type = get_object_or_404(ProgrameType,pk=programe_pk)
    produces_all_list = Produce.objects.filter(programe_type=programe_type)
    
    context = {}
    context['produces'] = produces_all_list

    context['produce_types'] = get_type_navigation()
    context['blog_types'] = get_type_blog()
    context['programe_types'] = get_programe_navigation()
    context['programe'] = programe_type
    context['produce_types_two'] = get_type_navigation_two()
    return render(request,'programe.html',context)

def produce_detail(request,produce_pk):
    context = {}
    produce = Produce.objects.filter(pk = produce_pk)
    context['produce'] = produce[0]

    context['produce_types'] = get_type_navigation()
    context['blog_types'] = get_type_blog()
    context['programe_types'] = get_programe_navigation()
    context['produce_types_two'] = get_type_navigation_two()
    return render(request,'produce_detail.html',context)


