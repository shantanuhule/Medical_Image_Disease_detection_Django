from django import forms
from .models import SkinDiseaseModel,ChestDiseaseModel,BrainTumorModel,KidneyDiseaseModel

class SkinDiseaseForm(forms.ModelForm):
    class Meta:
        model=SkinDiseaseModel
        exclude = ['p_disease']
        # fields = ['p_id', 'p_name', 'p_email', 'p_image','p_disease']
        labels={
            'p_id':"Patient ID",
            'p_name':"Patient Name",
            'p_email': "Patient Email",
            # 'p_disease':"Patient Disease"
        }

class ChestDiseaseForm(forms.ModelForm):
    class Meta:
        model=ChestDiseaseModel
        # fields =  ['p_id', 'p_name', 'p_email', 'p_image']
        exclude = ['p_disease']
        labels={
            'p_id':"Patient ID",
            'p_name':"Patient Name",
            'p_email': "Patient Email",
            # 'p_disease':"Patient Disease"
        }

class BrainTumorForm(forms.ModelForm):
    class Meta:
        model=BrainTumorModel
        # fields =  ['p_id', 'p_name', 'p_email', 'p_image']
        exclude = ['p_disease']
        labels={
            'p_id':"Patient ID",
            'p_name':"Patient Name",
            'p_email': "Patient Email",
            # 'p_disease':"Patient Disease"
        }

class KidenyDiseaseForm(forms.ModelForm):
    class Meta:
        model=KidneyDiseaseModel
        # fields =  ['p_id', 'p_name', 'p_email', 'p_image']
        exclude = ['p_disease']
        labels={
            'p_id':"Patient ID",
            'p_name':"Patient Name",
            'p_email': "Patient Email",
            # 'p_disease':"Patient Disease"
        }