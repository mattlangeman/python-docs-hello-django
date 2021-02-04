from django.template.response import TemplateResponse

from django.conf import settings

from .models import FileUpload

def hello(request):

    file_upload = FileUpload.objects.get(pk=1)

    context = {
        'DJANGO_GETS_ENV': settings.DJANGO_GETS_ENV,
        'DJANGO_OTHER_ENV_VAR': settings.DJANGO_OTHER_ENV_VAR,
        'file_upload': file_upload

    }
    response = TemplateResponse(request, 'hello/hello.html', context)
    return response
