from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from .models import Genre, Actor, TheatreHall, Play, Performance, Reservation
from .serializers import (
    GenreSerializer,
    ActorSerializer,
    TheatreHallSerializer,
    PlaySerializer,
    PerformanceSerializer,
    ReservationSerializer,
    PlayListSerializer,
    PlayDetailSerializer,
    PerformanceDetailSerializer,
    PerformanceListSerializer,
)


class GenreViewSet(GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class TheatreHallViewSet(
    GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin
):
    queryset = TheatreHall.objects.all()
    serializer_class = TheatreHallSerializer


class PlayViewSet(
    GenericViewSet,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
):
    queryset = Play.objects.all()
    serializer_class = PlaySerializer

    def get_serializer_class(self):
        if self.action == "list":
            return PlayListSerializer

        if self.action == "retrieve":
            return PlayDetailSerializer

        return PlaySerializer


class PerformanceViewSet(
    GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return PerformanceListSerializer

        if self.action == "retrieve":
            return PerformanceDetailSerializer

        return PerformanceSerializer


class ReservationViewSet(
    GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin
):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
