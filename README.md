---

# NotesNest

Welcome to **NotesNest**, your personal sticky notes application designed to help you create, edit, delete, and view notes. This is my first full-stack application built using Python, HTML, CSS, Bootstrap, and the Django web framework.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation and Setup](#installation-and-setup)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Unit Testing](#unit-testing)
- [Project Structure](#project-structure)

## Project Overview

**NotesNest** is a web-based application that allows users to manage their personal notes efficiently. With this app, you can:

- Create new notes
- Edit existing notes
- Delete notes you no longer need
- View all your notes in a consolidated hub

## Features

- **User Authentication**: Register and login to manage your notes securely.
- **CRUD Operations**: Full Create, Read, Update, and Delete functionality for notes.
- **Responsive Design**: Built using Bootstrap to ensure the application works well on all devices.
- **Unit Testing**: Comprehensive unit tests are implemented to ensure application stability and functionality.

## Technologies Used

- **Backend**: Python, Django
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite (default for Django development)

## Installation and Setup

Follow these steps to set up and run **NotesNest** on your local machine.

### Prerequisites

- Python 3.x installed on your system
- Virtual environment tools like `venv` or `virtualenv`

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/umarhuss/sticky_notes
   cd notesnest
   ```

2. **Create and Activate a Virtual Environment**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

3. **Install Required Dependencies**

   The project dependencies are listed in the `requirements.txt` file. Install them with:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**

   To set up the database and apply migrations, run:

   ```bash
   python manage.py migrate
   ```

## Running the Application

To start the Django development server, use the following command:

```bash
python manage.py runserver
```

Once the server is running, you can open your browser and navigate to `http://127.0.0.1:8000/` to access the application.

## Usage

1. **Register**: Click on the `Register` link to create a new account.
2. **Login**: Use the `Login` link to access your account.
3. **Manage Notes**: After logging in, you can start creating, editing, and deleting your notes from the `Notes Hub`.
4. **User Actions**:
   - **Add Note**: Use the `Add Note` button to create a new note.
   - **Edit Note**: Click on a note's title to view and edit its content.
   - **Delete Note**: Click the delete button to remove a note.

## Unit Testing

The project includes unit tests for the core functionalities to ensure everything works as expected. These tests cover models, views, and forms. To run the tests, use the following command:

```bash
python manage.py test
```

## Project Structure

- **models.py**: Contains the `StickyNote` model defining the note's schema.
- **views.py**: Handles the request and response logic for CRUD operations.
- **forms.py**: Contains the `StickyNoteForm` for creating and updating notes.
- **urls.py**: Maps URL patterns to their respective views.
- **templates/**: Contains HTML templates for different pages.
- **static/**: Stores static files like CSS.

Thank you for checking out **NotesNest**! Enjoy managing your notes efficiently with this simple and effective application.

---


