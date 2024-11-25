from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    if request.method == "GET":
        return Response({"message": "root of the api"})
