from drf_yasg.utils import no_body, swagger_auto_schema as schema
from drf_yasg.openapi import IN_QUERY, TYPE_BOOLEAN, TYPE_STRING, Parameter
from rest_framework import status

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, mixins
from rest_framework.permissions import AllowAny

from . import models, serializers


class BoardTest(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):

    queryset = models.Board.objects.all()
    permission_classes = [AllowAny]
    serializer_class = serializers.BoardTestSerializer

    @schema(
        operation_summary="board test",
        operation_description="""
        ### 세부내역
        """,
        tags=["board"],
        manual_parameters=[
            Parameter("title", IN_QUERY, type=TYPE_STRING, description="제목"),
        ],
    )
    def list(self, request, *args, **kwargs):

        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @schema(
        operation_summary="board-test-post  ",
        request_body=serializers.BoardTestSerializer,
        tags=["partner_notice"],
        operation_description="test",
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
