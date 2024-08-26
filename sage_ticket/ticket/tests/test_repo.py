import pytest

from sage_ticket.ticket.models import Comment, Department, Issue
from sage_ticket.ticket.repository.generator import TicketDataGenerator


class TestTicketDataGenerator:
    @pytest.fixture(scope="class")
    def generator(self):
        return TicketDataGenerator()

    def test_create_departments(self, generator):
        departments = generator.create_department(2)
        assert len(departments) == 2
        assert Department.objects.count() == 2

    def test_create_issues(self, generator):
        users = generator.create_users(10)
        departments = generator.create_department(2)

        issues = generator.create_issue(10, users, departments)
        assert len(issues) == 10
        assert Issue.objects.count() == 10

    def test_create_comments(self, generator):
        # Create users, departments, and issues for generating comments
        users = generator.create_users(10)
        departments = generator.create_department(2)
        issues = generator.create_issue(10, users, departments)

        # Create comments and assert the number of created comments
        comments = generator.create_comment(10, users, issues)
        assert len(comments) == 10
        assert Comment.objects.count() == 10
