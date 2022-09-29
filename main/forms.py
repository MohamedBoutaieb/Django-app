from django import forms


class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=200, required=True)
    check = forms.BooleanField()


class Bank(forms.Form):
    balance = forms.FloatField(label="Amount", required=True,min_value=0)
    check = forms.BooleanField(label="security check",required=True,)
