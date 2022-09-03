from django import forms
from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')
        labels = {'text': "Your note's text:"}
        widget = {
            "title" : forms.TextInput(attrs={"class": "form-control my-5"}),
            "text" : forms.Textarea(attrs={"class": "form-control my-5"})
            }

    #funkcja sprawdzajaca czy w tytule jest slowo 'Django'
    def clean_title(self):
        title = self.cleaned_data['title']
        if "Django" not in title:
            raise forms.ValidationError("We only accept notes that have word 'Django' in the title")
        return title