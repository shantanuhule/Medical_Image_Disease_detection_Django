from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about-us/', views.about_us, name='about_us'),
    path('info/', views.info, name='info'),
    path('detection/', views.detection, name='detection'),
    path('chest-disease/', views.chest_disease_detect, name='chest_disease_detect'),
    path('brain-tumor/', views.brain_tumor_detect, name='brain_tumor_detect'),
    path('skin-disease/', views.skin_disease_detect, name='skin_disease_detect'),
    path('kidney-disease/', views.kidney_disease_detect, name='kidney_disease_detect'),
]
