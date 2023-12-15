from django import forms
from .models import Magazine

class MagazineForm(forms.ModelForm):
    class Meta:
        model = Magazine
        fields = ['title', 'cover_image', 'pdf_file', 'publication_date', 'description']