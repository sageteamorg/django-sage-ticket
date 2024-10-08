import pytest
from sage_ticket.models import Comment, Department, Issue
from sage_ticket.repository.generator import TicketDataGenerator


@pytest.mark.django_db
class TestTicketDataGenerator:
    @pytest.fixture(scope="class")
    def generator(self):
        return TicketDataGenerator()

    def test_create_departments(self, generator):
        departments = generator.create_department(2)
        assert len(departments) == 2
        assert Department.objects.count() != 0

    def test_create_issues(self, generator):
        users = generator.create_users(10)
        departments = generator.create_department(2)

        issues = generator.create_issue(10, users, departments)
        assert len(issues) == 10
        assert Issue.objects.count() != 0

    def test_create_comments(self, generator):
        users = generator.create_users(10)
        departments = generator.create_department(2)
        issues = generator.create_issue(10, users, departments)

        comments = generator.create_comment(10, users, issues)
        assert len(comments) == 10
        assert Comment.objects.count() != 0
