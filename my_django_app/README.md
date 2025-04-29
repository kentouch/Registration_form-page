# My Django App

This project is a Django web application designed for user registration with a responsive layout using Bootstrap 5. The application features a registration form that collects various user details and submits them to a Google Sheet in real-time.

## Project Structure

```
my_django_app
├── my_django_app
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── registration
│   ├── migrations
│   │   └── __init__.py
│   ├── static
│   │   ├── css
│   │   │   └── styles.css
│   │   └── images
│   │       └── placeholder.png
│   ├── templates
│   │   └── registration
│   │       └── index.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── manage.py
├── requirements.txt
└── README.md
```

## Features

- Two-section layout: Information display on the left and a registration form in the center.
- Responsive design using Bootstrap 5.
- Form fields include:
  - Delegate category (dropdown)
  - Firstname
  - Lastname
  - Email
  - Nationality
  - National ID
  - Phone number
  - Address
  - Organization
  - Position
  - Country of residence
  - Social activities (dropdown)
- Integration with Google Sheets for real-time data submission.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd my_django_app
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up your Google Sheets API credentials to enable form submissions.

5. Run the migrations:
   ```
   python manage.py migrate
   ```

6. Start the development server:
   ```
   python manage.py runserver
   ```

## Usage

- Navigate to `http://127.0.0.1:8000/` to access the registration page.
- Fill out the registration form and submit to see the data sent to Google Sheets.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes. 

## License

This project is licensed under the MIT License.