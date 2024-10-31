import json

from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    """
    API view for the home page (http://localhost:8000/api/)

    Notes:
    first parameter of view is instance of HttpRequest typically named request
    print(dir(request))  # print all attributes and methods of request
    """
    data = {}
    try:
        """
        json.loads(request.body) parse body (b'' byte string JSON) to dict
        json.loads() raises exception if JSON is invalid
        """
        data = json.loads(request.body)
    except Exception as e:
        print(e)

    """
    - "request.GET" is used to access query parameters
        - it's a QueryDict, dict of query parameters
    - "request.headers" is used to access headers
        - it's a dict of headers, previously (request.META)
    - request.content_type is used to access content type of request body
        - it's already in headers
        - eg. (application/json)
    """
    data["params"] = dict(request.GET)
    # data["headers"] = dict(request.headers)
    # data["content_type"] = request.content_type

    print(data)  # will display JSON data and query parameters
    return JsonResponse({"message": "Hello, World!"})
