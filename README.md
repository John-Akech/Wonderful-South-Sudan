Wonderful South Sudan

Welcome to the Wonderful South Sudan web application! This project aims to promote tourism and conservation efforts in South Sudan. The application showcases various tours, allows users to book tours, and provides a contact form for inquiries.

Table of Contents:


-Installation

-Configuration

-Usage

-Contributing

-Contact

Installation:

Prerequisites

Ensure you have the following installed on your system:

Python 3.8 or higher

Django 3.2 or higher

Git

Steps:

Clone the Repository:

git clone git@github.com:John-Akech/Wonderful-South-Sudan.git
cd Wonderful-South-Sudan

Create and Activate a Virtual Environment:

python -m venv env

source env/bin/activate   # On Windows, use `env\Scripts\activate`


Install Dependencies

Set Up the Database

python manage.py migrate


Run the Development Server

python manage.py runserver

The application should now be running at http://127.0.0.1:8000/.

Configuration:

Environment Variables

Create a .env file in the project root directory and add the following configuration:

.env

SECRET_KEY=your_secret_key_here

DEBUG=True

ALLOWED_HOSTS=127.0.0.1, .localhost

DATABASE_URL=sqlite:///db.sqlite3


Replace your secret key with a unique secret key. You can generate one using Django's get_random_secret_key method.

Static Files

Run the following command to collect static files:

python manage.py collectstatic

Usage:

Access the Admin Interface

Visit http://127.0.0.1:8000/admin and log in using the superuser credentials you created earlier. From the admin interface, you can manage tours, bookings, and contact inquiries.

Booking a Tour:

Users can book a tour by visiting the Book a Tour page, filling out the booking form, and submitting it.

Contact Form:

Users can send inquiries through the Contact Us page by filling out and submitting the contact form.

Contributing:

We welcome contributions! To contribute:

Fork the repository.

Create a new branch (git checkout -b feature-branch).

Make your changes.

Commit your changes (git commit -m 'Add some feature').

Push to the branch (git push origin feature-branch).

Open a pull request.

Contact:

For any inquiries or support, please reach out to us at:

Email: j.akech@alustudent.com

GitHub: John-Akech
