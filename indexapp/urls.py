from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='indexapp'),
    path('tmemsapp/', include('tmemsapp.urls')),
    path('casapp/', include('casapp.urls')),
    path('ceapp/', include('ceapp.urls')),
    path('iwsaasapp/', include('iwsaasapp.urls')),
    path('visiononeapp/', include('visiononeapp.urls')),
    path('srecalendarapp/', include('srecalendarapp.urls') )
]