# ElevaWeb Project

Welcome to the ElevaWeb project repository! This is a Django-based web application that serves as a content management system (CMS) for a website.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Description

ElevaWeb is a web application built using Django 3.1.14. It serves as a content management system (CMS) for managing and publishing content on a website. The project includes features such as managing pages, blog posts, newsletters, and more.

## Features

- Page Management: Create, edit, and organize website pages.
- Blog System: Publish and manage blog posts with rich text editing.
- Newsletter Subscription: Allow users to subscribe to newsletters.
- Contact Form: Provide a contact form for users to get in touch.
- Multilingual Support: Support for multiple languages using Django's i18n framework.

## Installation

1. Clone the repository: `git clone https://github.com/pablocodelia/elevaproductorawebpage.git/`
2. Create a virtual environment: `python3 -m venv venv`
3. Activate the virtual environment: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Apply migrations: `python manage.py migrate`

## Configuration

1. Rename `.env.example` to `.env` and configure your environment variables.
2. Adjust settings in `settings.py` as needed for your environment.

## Usage

1. Start the development server: `python manage.py runserver`
2. Access the admin panel: `http://localhost:8000/admin/`
3. Create superuser: `python manage.py createsuperuser`
4. Access the website: `http://localhost:8000/`

## Contributing

Contributions are welcome! If you find any issues or have suggestions, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
