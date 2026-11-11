from django import forms
from django.core.files.storage import default_storage

class UploadFileForm(forms.Form):
    #title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=50)
    #jmeno = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=50, label="Jméno")
    file = forms.FileField()

    def clean_file_save(self):
        uploaded_file = self.cleaned_data['file']
        saved_name = default_storage.save(f"uploads/{uploaded_file.name}", uploaded_file)
        return saved_name
