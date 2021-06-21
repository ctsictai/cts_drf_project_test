from drf_yasg.openapi import FORMAT_PASSWORD, IN_QUERY, TYPE_BOOLEAN, TYPE_STRING, Parameter  # noqa # isort
from drf_yasg.utils import no_body  # noqa
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import action  # noqa
from rest_framework.exceptions import ParseError  # noqa
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, mixins

from . import models, serializers


class BoardTest(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):

    queryset = models.Board.objects.all()
    permission_classes = [AllowAny]
    serializer_class = serializers.BoardTestSerializer

    @swagger_auto_schema(
        operation_summary="board test",
        operation_description="""
        ### 세부내역
        """,
        tags=["board"],
        manual_parameters=[
            Parameter("title", IN_QUERY, type=TYPE_STRING, description="제목"),
            Parameter(
                "test",
                IN_QUERY,
                type=TYPE_STRING,
                description="디스크립션_테스트",
                format=FORMAT_PASSWORD,
            ),
        ],
    )
    def list(self, request, *args, **kwargs):

        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        # raise ValueError("fsadfsf")

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="board-test-post  ",
        # request_body=serializers.BoardTestSerializer,
        tags=["board_create"],
        operation_description="post_test",
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
