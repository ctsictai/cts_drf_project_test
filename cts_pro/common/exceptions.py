# from django.core.exceptions import PermissionDenied
# from django.http import Http404
# from rest_framework import exceptions
# from rest_framework.response import Response
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    """
    Returns the response that should be used for any given exception.

    By default we handle the REST framework `APIException`, and also
    Django's built-in `Http404` and `PermissionDenied` exceptions.

    Any unhandled exceptions may return `None`, which will cause a 500 error
    to be raised.
    """
    response = exception_handler(exc, context)
    # print("exception_response :::: ", response)
    # print("WERWERW", response.data)
    if response is not None:
        response.data["success"] = "0"
        response.data["status_code"] = response.status_code
        response.data["results"] = response.data["detail"]
    else:
        data = {
            "success": "0",
            "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "results": "서버에러입니다. 관리자에게 문의 주세요.",
        }
        response = Response(data)
    return response
