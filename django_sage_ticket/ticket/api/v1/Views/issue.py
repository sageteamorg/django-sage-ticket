from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework import filters
from rest_framework.throttling import AnonRateThrottle
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

from django_filters.rest_framework import DjangoFilterBackend
from django_sage_ticket.ticket.api.v1.serializers import IssueSerializer
from django_sage_ticket.ticket.models import Issue


class Rghandler(AnonRateThrottle):
    THROTTLE_RATES = {"anon": "10/hour"}


class IssueViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = [
        "state",
        "name",
    ]

    search_fields = ["subject"]
    throttle_classes = [Rghandler]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
