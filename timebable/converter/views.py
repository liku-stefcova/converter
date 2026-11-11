from django.shortcuts import render
from django.http import HttpResponse
from . import forms

def upload_form(request):
    if request.method == 'POST':
        form = forms.UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            saved_name = form.clean_file_save()
            return HttpResponse(f"File saved successfully: {saved_name}")
    else:
        form = forms.UploadFileForm()
    context = {'form': form}
    return render(request, 'converter/upload_form.html', context )
