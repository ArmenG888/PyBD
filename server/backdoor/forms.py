from django import forms

class CodeForm(forms.Form):
    code = forms.CharField()

class ScreenShotForm(forms.Form):
    file = forms.FileField()

class OutputForm(forms.Form):
    output = forms.CharField()