from django.contrib import admin
from .models import Question,Choise

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id','question')

@admin.register(Choise)
class ChoiseAdmin(admin.ModelAdmin):
    list_display = ('id','question','c1','v1','c2','v2','c3','v3','c4','v4')
