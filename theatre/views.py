from rest_framework import mixins
from .serializers import GenreSerializer
from rest_framework.viewsets import GenericViewSet

from .models import (
    Genre,
)


class GenreViewSet(
    GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
