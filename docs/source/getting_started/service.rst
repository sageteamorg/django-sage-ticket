Service Layer
=============

The service layer contains the core logic for generating and handling ticketing data, including users, departments, issues, comments, and attachments. Below is a detailed description of the `TicketDataGenerator` class, including its methods, arguments, and usage examples.

TicketDataGenerator Class
-------------------------

The `TicketDataGenerator` class is designed to generate test data for various models in the ticketing system, such as users, departments, issues, comments, and attachments.

Methods
^^^^^^^

- `create_users(total: int) -> QuerySet`
  Generates a specified number of users and returns the queryset of the created users.

  **Arguments:**
  - `total`: The total number of users to generate.

  **Returns:**
  - `QuerySet`: A queryset of the created `User` instances.

- `create_department(total: int) -> QuerySet`
  Generates a specified number of departments and returns the queryset of the created departments.

  **Arguments:**
  - `total`: The total number of departments to generate.

  **Returns:**
  - `QuerySet`: A queryset of the created `Department` instances.

- `create_comment(total: int, users: QuerySet, issues: QuerySet) -> QuerySet`
  Generates a specified number of comments and returns the queryset of the created comments.

  **Arguments:**
  - `total`: The total number of comments to generate.
  - `users`: A queryset of `User` instances to associate with the comments.
  - `issues`: A queryset of `Issue` instances to associate with the comments.

  **Returns:**
  - `QuerySet`: A queryset of the created `Comment` instances.

- `create_issue(total: int, users: QuerySet, department: QuerySet) -> QuerySet`
  Generates a specified number of issues and returns the queryset of the created issues.

  **Arguments:**
  - `total`: The total number of issues to generate.
  - `users`: A queryset of `User` instances to associate with the issues.
  - `department`: A queryset of `Department` instances to associate with the issues.

  **Returns:**
  - `QuerySet`: A queryset of the created `Issue` instances.

- `create_attachment(total: int, issues: QuerySet) -> QuerySet`
  Generates a specified number of attachments and returns the queryset of the created attachments.

  **Arguments:**
  - `total`: The total number of attachments to generate.
  - `issues`: A queryset of `Issue` instances to associate with the attachments.

  **Returns:**
  - `QuerySet`: A queryset of the created `Attachment` instances.

- `get_random_f() -> List[Tuple[str, bytes]]`
  Retrieves a list of random files from the demo directory.

  **Returns:**
  - `List[Tuple[str, bytes]]`: A list of tuples containing the file path and its content as bytes.

- `add_2_m_m(objs: List[Any], target_field: str, item_per_obj: int, item: Any) -> None`
  Adds a specified number of items to a Many-to-Many field of a model instance.

  **Arguments:**
  - `objs`: A list of objects to add.
  - `target_field`: The field name of the target model.
  - `item_per_obj`: The number of items to add per object.
  - `item`: The target object to which items will be added.

- `join_members(department: QuerySet, members: QuerySet, total: int) -> QuerySet`
  Associates members with departments and returns the updated departments.

  **Arguments:**
  - `department`: A queryset of `Department` instances.
  - `members`: A queryset of `User` instances to associate with the departments.
  - `total`: The number of members to associate with each department.

  **Returns:**
  - `QuerySet`: The updated queryset of `Department` instances.

Example Usage
^^^^^^^^^^^^^

.. code-block:: python

    from django_sage_ticket.ticket.services import TicketDataGenerator

    # Create an instance of TicketDataGenerator
    data_generator = TicketDataGenerator()

    # Generate users
    users = data_generator.create_users(total=100)

    # Generate departments
    departments = data_generator.create_department(total=10)

    # Generate issues
    issues = data_generator.create_issue(total=50, users=users, department=departments)

    # Generate comments
    comments = data_generator.create_comment(total=200, users=users, issues=issues)

    # Generate attachments
    attachments = data_generator.create_attachment(total=150, issues=issues)

    # Associate members with departments
    updated_departments = data_generator.join_members(department=departments, members=users, total=5)
