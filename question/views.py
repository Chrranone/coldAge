from django.shortcuts import render
from navigation.views import get_type_navigation,get_type_navigation_two
from blog.views import get_type_blog,get_programe_navigation
from .models import Choise

def questions(request):
    context = {}

    choises = Choise.objects.all()

    context['choises'] = choises
    context['produce_types'] = get_type_navigation()
    context['blog_types'] = get_type_blog()
    context['programe_types'] = get_programe_navigation()
    context['produce_types_two'] = get_type_navigation_two()
    return render(request,'questions.html',context)
