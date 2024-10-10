import json

from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    """
    API view for the home page (http://localhost:8000/api/)

    Notes:
    first parameter of view is instance of HttpRequest typically named request
    print(dir(request))  # print all attributes and methods of request
    """
    print(request.GET)  # dictionary of query parameters
    body = request.body  # byte string (b'') of JSON data
    data = {}
    try:
        data = json.loads(body)  # parse the body (JSON) -> dictionary
    except Exception as e:
        print(e)

    data["params"] = dict(request.GET)
    data["headers"] = dict(request.headers)
    data["content_type"] = request.content_type
    print(data)
    return JsonResponse({"message": "Hello, World!"})
