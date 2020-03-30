from django import forms
from .models import tamashii


class SearchForm(forms.Form):
    search_bun = forms.CharField(label="", max_length=30)


class UpdateForm(forms.ModelForm):

    class Meta:
        model = tamashii
        fields = ['name', 'country', 'sex', 'dormitory', 'room', 'evangelist', 'school', 'status']
        exclude = ('date',)
