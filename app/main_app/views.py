from django.http import HttpResponse


def health(request):
    return HttpResponse('success', content_type="application/json")
