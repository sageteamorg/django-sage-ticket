from rest_framework.serializers import ModelSerializer
from django_sage_ticket.ticket.models import Issue, Department, Comment, Attachment


class ParentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = ["title" "description"]


class ReplaySerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ["replay"]


class IssueSerializer(ModelSerializer):
    user = ParentSerializer

    class Meta:
        model = Issue
        depth = 1
        fields = "__all__"


class CommentSerializer(ModelSerializer):
    user = ReplaySerializer

    class Meta:
        model = Comment
        depth = 1
        fields = "__all__"


class AttachmentSerializer(ModelSerializer):
    class Meta:
        model = Attachment
        fields = "__all__"


class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"
