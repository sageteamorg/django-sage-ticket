from rest_framework.viewsets import GenericViewSet
from rest_framework.pagination import PageNumberPagination

from rest_framework.mixins import ListModelMixin, RetrieveModelMixin

from rest_framework import filters
from rest_framework.throttling import AnonRateThrottle

from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

from django_filters.rest_framework import DjangoFilterBackend

from ..Serializers import DepartmentSerializer
from django_sage_ticket.ticket.models import Department


class LargeIssuePagination(PageNumberPagination):
    page_size = 2
    page_query_param = "page"
    page_size_query_param = "page_size"
    max_page_size = 10


class Rghandler(AnonRateThrottle):
    THROTTLE_RATES = {"anon": "10/hour"}


class DepartmentViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Department.objects.all()

    serializer_class = DepartmentSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = [
        "member",
    ]

    search_fields = ["name"]

    throttle_classes = [Rghandler]

    permission_classes = [IsAuthenticated, DjangoModelPermissions]
