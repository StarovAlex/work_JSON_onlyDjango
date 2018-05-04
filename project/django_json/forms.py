from django import forms


class JSONForm(forms.Form):
    json_data = forms.CharField(widget=forms.Textarea)
