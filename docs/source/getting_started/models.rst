Models Layer
============

The models layer defines the database models for the ticketing system. These models represent various entities such as departments, issues, comments, and attachments, and are integrated into Django's admin interface.

Department
----------

The `Department` model represents a department within an organization. Departments are associated with members who are users in the system.

Fields
^^^^^^

- `title`: The title of the department.
- `description`: A description of the department.
- `member`: The members of the department (Many-to-Many relationship with users).

Attachment
----------

The `Attachment` model represents attachments related to issues. Attachments can include various types of files with different extensions.

Fields
^^^^^^

- `name`: The name of the attachment.
- `issue`: The issue to which this attachment is related.
- `extensions`: The file extension of the attachment.
- `file`: The file that is uploaded.

Comment
-------

The `Comment` model represents comments related to issues. Comments are made by users and can be linked to specific issues.

Fields
^^^^^^

- `title`: The title of the comment.
- `user`: The user who made the comment.
- `issue`: The issue to which this comment is related.
- `message`: The content of the comment.
- `is_unread`: Indicates if the comment is unread.
- `status`: The status of the comment (e.g., Answered, Unanswered).
- `replay`: The comment to which this is a reply (optional).

Issue
-----

The `Issue` model represents an issue in the ticketing system. Issues are reported by users and can be assigned to departments.

Fields
^^^^^^

- `subject`: The subject of the issue.
- `name`: The name of the issue reporter.
- `message`: The detailed message of the issue.
- `severity`: The severity level of the issue.
- `raised_by`: The user who raised the issue.
- `department`: The department to which the issue is assigned.
- `state`: The current state of the issue (e.g., New, Open, Pending).
- `is_unread`: Indicates if the issue is unread.
- `is_archive`: Indicates if the issue is archived.

Admin Integration
-----------------

To integrate these models into the Django admin interface, register them in the `admin.py` file of your app.

.. code-block:: python

    from django.contrib import admin
    from django_sage_ticket.ticket.models import Department, Attachment, Comment, Issue

    @admin.register(Department)
    class DepartmentAdmin(admin.ModelAdmin):
        list_display = ['title', 'created']
        search_fields = ['title']
        readonly_fields = ['created', 'modified']
        autocomplete_fields = ['member']

    @admin.register(Attachment)
    class AttachmentAdmin(admin.ModelAdmin):
        list_display = ['name', 'issue', 'extensions', 'file', 'created']
        list_filter = ['extensions', 'created']
        search_fields = ['name', 'issue__title']
        readonly_fields = ['created', 'modified']

    @admin.register(Comment)
    class CommentAdmin(admin.ModelAdmin):
        list_display = ['title', 'user', 'issue', 'status', 'is_unread', 'created']
        list_filter = ['status', 'is_unread', 'created']
        search_fields = ['title', 'user__username', 'issue__title']
        readonly_fields = ['created', 'modified']

    @admin.register(Issue)
    class IssueAdmin(admin.ModelAdmin):
        list_display = ['subject', 'state', 'created']
        list_filter = ['state', 'created']
        search_fields = ['subject', 'description']
        readonly_fields = ['created', 'updated']

This will allow you to manage the different models directly from the Django admin interface.
