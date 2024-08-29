
# Django Sage Ticket

Django Sage Ticket is a Django application for managing issues, comments, attachments, and departments within an organization. It provides a comprehensive admin interface to create, view, and manage tickets and their associated components, along with a robust state machine for handling ticket states.

## Features

- Create and manage tickets with detailed descriptions, severity levels, and state transitions.
- Associate tickets with specific departments and users within the organization.
- Add comments to tickets, supporting threaded replies and unread status indicators.
- Attach files to tickets with support for various file extensions.
- Automatically generate test data for tickets, users, departments, and comments using the provided data generator.
- Extendable state management system, allowing for custom state transitions and validation.

## Installation

### Using `pip` with `virtualenv`

1. **Create a Virtual Environment**:

    ```bash
    python -m venv .venv
    ```

2. **Activate the Virtual Environment**:

   - On Windows:

     ```bash
     .venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source .venv/bin/activate
     ```

3. **Install `django-sage-ticket`**:

    ```bash
    pip install django-sage-ticket
    ```

### Using `poetry`

1. **Initialize Poetry** (if not already initialized):

    ```bash
    poetry init
    ```

2. **Install `django-sage-ticket`**:

    ```bash
    poetry add django-sage-ticket
    ```

3. **Apply Migrations**:

    After installation, make sure to run the following commands to create the necessary database tables:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

## Configuration

### Django Settings

Add `django-sage-ticket` to your `INSTALLED_APPS` in the Django settings:

```python
INSTALLED_APPS = [
    ...
    "sage_ticket",
    ...
]
```

## Usage

### Admin Interface

The package provides an admin interface to manage all aspects of the ticketing system:

- **Issues**: Create, view, and manage tickets, associate them with departments, and handle state transitions.
- **Comments**: Add comments to tickets, manage threads, and mark comments as read or unread.
- **Attachments**: Attach files to tickets and manage their extensions.
