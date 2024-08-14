from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework import filters
from rest_framework.throttling import AnonRateThrottle
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from django_filters.rest_framework import DjangoFilterBackend

from django_sage_ticket.ticket.api.v1.serializers import AttachmentSerializer
from django_sage_ticket.ticket.models import Attachment


class Rghandler(AnonRateThrottle):
    THROTTLE_RATES = {"anon": "10/hour"}


class AttachmentViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = [
        "extensions",
        "name",
    ]

    search_fields = ["file"]

    throttle_classes = [Rghandler]

    permission_classes = [IsAuthenticated, DjangoModelPermissions]
