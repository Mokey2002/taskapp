
# Task App
## Description
This is a simple task management web application built using Django for the backend and React for the frontend. The app allows users to:
- Create tasks
- View a list of tasks
- Update tasks (mark as completed)
- Delete tasks

## Setup Instructions

### Backend (Django)
1. Navigate to the backend directory:
   ```
   cd taskapp
   ```
2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install django
   ```
4. Run migrations to set up the database:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Start the Django development server:
   ```
   python manage.py runserver
   ```

### Frontend (React)
1. Navigate to the frontend directory:
   ```
   cd frontend
   ```
2. Install dependencies:
   ```
   npm install
   ```
3. Start the React development server:
   ```
   npm start
   ```

## Usage
1. Start the Django backend server and React frontend server as described above.
2. Open your browser and go to `http://localhost:3000` to access the app.

## Project Structure
```
taskapp/    # Backend (Django)
    tasks/      # Contains models, views, and URLs for task management
frontend/       # Frontend (React)
    src/        # Contains React components
```

## Features
- Very simple UI for managing tasks
- Backend APIs using Django
- React frontend for user interaction
- MySQL database
