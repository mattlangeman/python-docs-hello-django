from django.template.response import TemplateResponse

from django.conf import settings

from .models import FileUpload

def hello(request):

    file_upload = FileUpload.objects.get(pk=1)

    context = {
        'file_upload': file_upload
    }
    response = TemplateResponse(request, 'hello/hello.html', context)
    return response
