from django import forms
from agenda.models import Cursus, StudyPeriod

class CursusForm(forms.ModelForm):
    """The cursus Administration form"""
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'class':'datepicker'})
    )
    
    class Meta:
        model = Cursus

class StudyPeriodForm(forms.ModelForm):
    """The Study Period Administration form"""
    
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'class':'datepicker'})
    )
    end_date = forms.DateField(
        widget=forms.DateInput(attrs={'class':'datepicker'})
    )
    class Meta:
        model = StudyPeriod
