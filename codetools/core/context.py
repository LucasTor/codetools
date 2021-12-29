from django.conf import settings

def version_processor(request):
    return {
       "app_version": settings.APP_VERSION,
    }