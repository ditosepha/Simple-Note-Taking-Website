from django import forms
from .models import Note
from django.utils import timezone

class AddNoteForm(forms.ModelForm):
    title = forms.CharField(label='Title', max_length=50, widget=forms.TextInput(attrs={'size': '40'}))
    content = forms.CharField(label='Content', widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))
    
    class Meta:
        model = Note
        fields = ['title', 'content', 'data_created']