from django import forms 
from django.forms.widgets import NumberInput
import datetime

birth_years = ['1999','2000','2001','2002']
fav_colors = [
    ('blue','Blue'),
    ('green','Green'),
    ('black','Black'),
]

class UserForm(forms.Form):
    first_name = forms.CharField(max_length=20,initial="Your name")  
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    email = forms.EmailField(required=False, label="Please enter your email address")
    agree = forms.BooleanField(initial=True)
    date = forms.DateField()
    birth_date = forms.DateField(widget=NumberInput(attrs={'type':'date'}))
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=birth_years))
    value = forms.DecimalField()
    message = forms.CharField(max_length=10)
    day = forms.DateField(initial=datetime.date.today)
    fav_color = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=fav_colors)
    

    






