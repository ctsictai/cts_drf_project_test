from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):

    handlers = {
        "ValueError": _handle_generic_error,
        "AttributeError": _handle_generic_error,
    }

    response = exception_handler(exc, context)
    # print("exception_response :::: ", response)
    # print("WERWERW", response.data)
    if response is not None:
        response.data["success"] = "0"
        response.data["status_code"] = response.status_code
        response.data["results"] = response.data["detail"]
        return response

    exception_class = exc.__class__.__name__
    # print(exception_class)
    if exception_class in handlers:
        return handlers[exception_class](exc, context, response)

    if response is None:
        data = {
            "success": "0",
            "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "results": "서버에러입니다. 관리자에게 문의 주세요.",
            "detail": exc.args[0],
        }
        return Response(data)


def _handle_generic_error(exc, context, response):
    # print(response)
    # print("exception :::", exc.args)
    data = {
        "success": "0",
        "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
        "results": "서버에러입니다. 관리자에게 문의 주세요.",
        "detail": exc.args[0],
    }
    return Response(data)
