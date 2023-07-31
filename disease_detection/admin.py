from django.contrib import admin

# Register your models here.
from .models import ChestDiseaseModel

class ChestDAdmin(admin.ModelAdmin):
    list_display=("p_id","p_name","p_email","p_disease")

admin.site.register(ChestDiseaseModel,ChestDAdmin)