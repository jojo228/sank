# forms.py
from django import forms


class SearchForm(forms.Form):
    city = forms.CharField(required=False)
    guests = forms.IntegerField(required=False)
    check_in = forms.DateField(required=False)
    check_out = forms.DateField(required=False)

    

