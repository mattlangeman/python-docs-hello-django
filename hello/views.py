from django.template.response import TemplateResponse

from django.conf import settings

def hello(request):
    context = {
        'DJANGO_GETS_ENV': settings.DJANGO_GETS_ENV,
        'DJANGO_OTHER_ENV_VAR': settings.DJANGO_OTHER_ENV_VAR
    }
    response = TemplateResponse(request, 'hello/hello.html', context)
    return response
