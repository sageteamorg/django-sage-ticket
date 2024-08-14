from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework import filters
from rest_framework.throttling import AnonRateThrottle
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from django_filters.rest_framework import DjangoFilterBackend

from django_sage_ticket.ticket.api.v1.serializers import CommentSerializer
from django_sage_ticket.ticket.models import Comment


class Rghandler(AnonRateThrottle):
    THROTTLE_RATES = {"anon": "10/hour"}


class CommentViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = [
        "status",
        "issue",
    ]

    search_fields = ["message"]

    throttle_classes = [Rghandler]

    permission_classes = [IsAuthenticated, DjangoModelPermissions]
