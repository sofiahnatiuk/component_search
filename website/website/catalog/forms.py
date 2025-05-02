from django import forms
from .models import Report


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['comment']

    comment = forms.CharField(
        label='Будь ласка, опишіть проблему з даним компонентом:',
        widget=forms.Textarea(attrs={
            'placeholder': 'Ваш коментар...',
            'rows': 10,
            'cols': 150
        })
    )