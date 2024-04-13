from .models import RegMP,feedback,reservation
from django.forms import ModelForm, TextInput,Textarea
from django import forms
from datetime import datetime
from django.utils import timezone

class ForMPForm(ModelForm):
    class Meta:
        model = RegMP
        fields = ['name','sername','email']
        widgets = {
        "name": TextInput(attrs={'class': 'uk-input uk-form-width-medium','placeholder': 'Имя'}),
        "sername": TextInput(attrs={'class': 'uk-input uk-form-width-medium','placeholder': 'Фамилия'}),
        "email": TextInput(attrs={'class': 'uk-input uk-form-width-large','placeholder': 'email'}),
        }
class Forfeedback(ModelForm):
    class Meta:
        model = feedback
        fields = ['name','sername','email','text']
        widgets = {
        "name": TextInput(attrs={'class': 'uk-input uk-form-width-medium','placeholder': 'Имя'}),
        "sername": TextInput(attrs={'class': 'uk-input uk-form-width-medium','placeholder': 'Фамилия'}),
        "email": TextInput(attrs={'class': 'uk-input uk-form-width-large','placeholder': 'email'}),
        "text": Textarea(attrs={'class': 'uk-textarea','placeholder': 'Ввод текста','rows': 10}),
        }
class ForReservation(forms.Form):
    date = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'datetime-local','class':'uk-input'}), localize=True,input_formats=['%Y-%m-%dT%H:%M'])
    name = forms.CharField(max_length=20,widget = forms.TextInput(attrs = {'class':'uk-input','placeholder' : 'Имя'}))
    sername = forms.CharField(max_length=20,widget = forms.TextInput(attrs = {'class':'uk-input','placeholder' : 'Фамилия'}))
    number = forms.CharField(max_length=20,widget = forms.TextInput(attrs = {'class':'uk-input','placeholder' : 'Номер телефона'}))
    table1 = forms.BooleanField(widget = forms.CheckboxInput(attrs={'class':'hidden_checkbox tc2'}),required=False)
    table2 = forms.BooleanField(widget = forms.CheckboxInput(attrs={'class':'hidden_checkbox tc1'}),required=False)
    table3 = forms.BooleanField(widget = forms.CheckboxInput(attrs={'class':'hidden_checkbox tc2'}),required=False)
    table4 = forms.BooleanField(widget = forms.CheckboxInput(attrs={'class':'hidden_checkbox tc2'}),required=False)
    table5 = forms.BooleanField(widget = forms.CheckboxInput(attrs={'class':'hidden_checkbox tc2'}),required=False)
    table6 = forms.BooleanField(widget = forms.CheckboxInput(attrs={'class':'hidden_checkbox tc2'}),required=False)
    table7 = forms.BooleanField(widget = forms.CheckboxInput(attrs={'class':'hidden_checkbox tc1'}),required=False)
    table8 = forms.BooleanField(widget = forms.CheckboxInput(attrs={'class':'hidden_checkbox tc2'}),required=False)
    table9 = forms.BooleanField(widget = forms.CheckboxInput(attrs={'class':'hidden_checkbox tc2'}),required=False)
    table10 = forms.BooleanField(widget = forms.CheckboxInput(attrs={'class':'hidden_checkbox tc1'}),required=False)
