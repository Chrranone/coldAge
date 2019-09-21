from django.shortcuts import render,redirect
from navigation.models import HomeImage
from navigation.views import get_type_navigation,get_programe_navigation,get_type_navigation_two
from blog.views import get_type_blog

def home(request):
    homeimage = HomeImage.objects.all()
    context = {
        'hms' : homeimage
    }

    context['produce_types'] = get_type_navigation()
    context['blog_types'] = get_type_blog()
    context['programe_types'] = get_programe_navigation()
    context['produce_types_two'] = get_type_navigation_two()
    
    return render(request,'home.html',context)
    