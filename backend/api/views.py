from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    return JsonResponse({"data": "Hello World!"})