from django.contrib import admin
from .models import HomeImage
from django.utils.safestring import mark_safe
# Register your models here.

class HomeImageAdmin(admin.ModelAdmin):

    def image_date(self,obj):
        try:
            #img = mark_safe("<img src='{% "+"static "+ "'"+(obj.image.url,)+"'" +" %}"+" width='50px' />" )
            img = mark_safe("<img src='static/media/%s' width='50px' />" % (obj.image.url,))
        except Exception as e:
            img = ''

        return img

    list_display = ['title','image_date']

    readonly_fields = ['image_date']

admin.site.register(HomeImage,HomeImageAdmin)

