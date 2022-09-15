from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.srecalendarapp, name='srecalendarapp'),
    path('deleteoffset/<int:id>', views.deleteoffset, name='deleteoffset'),
    path('deletecalender/<int:id>', views.deletecalender, name='deletecalender'),
]