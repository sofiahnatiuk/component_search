from django import forms
from .models import Report, Component, Category


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


class ComponentForm(forms.ModelForm):
    class Meta:
        model = Component
        fields = [
            'name', 'manufacturer', 'category', 'description',
            'package_type', 'operating_voltage', 'operating_current', 'power'
        ]
        labels = {
            'name': 'Назва',
            'manufacturer': 'Виробник',
            'category': 'Категорія',
            'description': 'Опис',
            'package_type': 'Тип корпусу',
            'operating_voltage': 'Робоча напруга (V)',
            'operating_current': 'Робочий струм (A)',
            'power': 'Потужність (W)',
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'parent', 'description']
        labels = {
            'name': 'Назва категорії',
            'parent': 'Батьківська категорія',
            'description': 'Опис (необовʼязково)',
        }
