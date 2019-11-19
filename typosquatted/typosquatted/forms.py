from django import forms

class WebForm(forms.Form):
    weburl = forms.CharField(label='Website Url', max_length=100)