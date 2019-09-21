from django.urls import path
from . import views

urlpatterns = [
    path('type/<int:produce_type_pk>',views.produce_list,name="produce_list"),
    path('type_two/<int:produce_type_two_pk>',views.produce_list_two,name="produce_list_two"),
    path('detail/<int:produce_pk>',views.produce_detail,name='produce_detail'),
    path('programe/<int:programe_pk>',views.programe,name='programe'),
]
