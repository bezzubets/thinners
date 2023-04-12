from django import forms
from .models import Thinners, Ukr_thinners


class OrderForm(forms.Form):
    name = forms.ModelChoiceField(empty_label='Выберите растворитель', label='Импортный растворитель',
                                  queryset=Thinners.objects.all(), required=False,
                                  widget=forms.Select(attrs={"class": "form-control"}))
    ukr_name = forms.ModelChoiceField(empty_label='Выберите растворитель', label='Украинский растворитель',
                                      queryset=Ukr_thinners.objects.all(), required=False,
                                      widget=forms.Select(attrs={"class": "form-control"}))
    purpose = forms.CharField(label='Количество в килограммах',
                              widget=forms.TextInput(attrs={"class": "form-control"}))
    description = forms.CharField(
        label='Здесь, напишите пожалуйста пожелания по доставке, срокам поставки, и укажите контакты для обратной связи',
        required=False,
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 5}))


class FeedbackForm(forms.Form):
    fio = forms.CharField(label='Ваше ФИО, и название организации',
                          widget=forms.TextInput(attrs={"class": "form-control"}))
    mail = forms.EmailField(label='Электронная почта', widget=forms.TextInput(attrs={"class": "form-control"}))
    phone = forms.CharField(label='Номер телефона, пожалуйста', widget=forms.TextInput(attrs={"class": "form-control"}))
    text = forms.CharField(label='Текст обращения', widget=forms.Textarea(attrs={"class": "form-control", "rows": 5}))
