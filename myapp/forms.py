from django import forms

class CreateForm(forms.Form):
    name = forms.CharField(max_length=200, label="Titulo")
    description = forms.CharField(widget=forms.Textarea, 
                                  label="Descripción", 
                                  required=False)