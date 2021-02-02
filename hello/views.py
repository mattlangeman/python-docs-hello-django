from django.http import HttpResponse
from django.conf import settings

def hello(request):
    return HttpResponse("Hello, World! %s" % (settings.DJANGO_GETS_ENV))
