from rest_framework.serializers import ModelSerializer

from . import models


class BoardTestSerializer(ModelSerializer):
    class Meta:
        model = models.Board
        fields = "__all__"
