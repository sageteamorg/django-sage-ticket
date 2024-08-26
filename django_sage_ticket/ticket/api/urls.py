from rest_framework import routers
from .v1 import IssueViewSet, CommentViewSet, DepartmentViewSet, AttachmentViewSet

router = routers.DefaultRouter()
router.register(r"Issue", IssueViewSet)
router.register(r"comment", CommentViewSet)
router.register(r"attachment", AttachmentViewSet)
router.register(r"department", DepartmentViewSet)

urlpatterns = router.urls
