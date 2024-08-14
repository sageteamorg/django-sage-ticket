from rest_framework.viewsets import GenericViewSet
from rest_framework.pagination import PageNumberPagination

from rest_framework.mixins import ListModelMixin, RetrieveModelMixin

from rest_framework import filters
from rest_framework.throttling import AnonRateThrottle

from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

from django_filters.rest_framework import DjangoFilterBackend

from ..Serializers import AttachmentSerializer
from django_sage_ticket.ticket.models import Attachment


class LargeIssuePagination(PageNumberPagination):
    page_size = 2
    page_query_param = "page"
    page_size_query_param = "page_size"
    max_page_size = 10


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
        "extenstions",
        "name",
    ]

    search_fields = ["file"]

    throttle_classes = [Rghandler]

    permission_classes = [IsAuthenticated, DjangoModelPermissions]
