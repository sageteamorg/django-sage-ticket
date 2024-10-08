import pytest
from sage_ticket.models import Issue
from sage_ticket.repository.manager.ticketing import DataAccessLayerManager


@pytest.mark.django_db
@pytest.fixture
def manager():
    return DataAccessLayerManager()


@pytest.mark.django_db
class TestDataAccessLayerManager:
    def test_get_queryset_returns_custom_queryset(self, manager):
        queryset = manager.get_queryset()
        assert isinstance(
            queryset, manager.get_queryset().__class__
        ), f"Expected queryset to be instance of TicketingQueryAccess, got {type(queryset)}"

    def test_filter_by_department(self, manager):
        department_id = 1
        issues = Issue.objects.filter(department_id=department_id)
        for issue in issues:
            assert (
                issue.department_id == department_id
            ), f"Expected department_id {department_id}, but got {issue.department_id}"

    def test_find_by_publisher(self, manager):
        user_id = 2
        issues = Issue.objects.filter(raised_by_id=user_id)
        for issue in issues:
            assert (
                issue.raised_by_id == user_id
            ), f"Expected raised_by_id {user_id}, but got {issue.raised_by_id}"
