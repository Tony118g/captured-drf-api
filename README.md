# Captured - API

Captured is a content sharing platform for photographers. Users can showcase their own photographs along with details concerning them and interact with other users via likes, comments and follows. The site is also used as an advertising platform for the site admin to share photographic tour opportunities that users can choose to attend.

This repository contains the backend API setup built to support the ReactJS frontend and is powered by the Django Rest Framework.

* [Project Goals](#project-goals)
* [Technologies Used](#technologies-used)

## Project Goals
This section of the project provides a Django Rest Framework API for the [Captured React web app](https://github.com/Tony118g/captured). The primary goals that this section of the project aims to achieve are as follows:

* Provide a fully functional API for the front-end to connect to and use.
* Provide a connection to necessary services along with relevant functionality to ensure correct data and media storage.
    * Create and provide access to a well structured database.
    * Connect to cloudinary and wire up relevant functionality for media storage.
* Include base functionality for authentiction.
* Include base functionality for form validation.
* Provide the means for crud operations where necessary.

Goals pertaining to the entire project can be found [here](https://github.com/Tony118g/captured#project-goals).

## Technologies Used

### Languages
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
    * The programming language used.

### Libraries and Frameworks
* [Django REST Framework](https://www.django-rest-framework.org/)
    * The framework used to create the API.
* [Django](https://pypi.org/project/Django/)
    * The framework used to help develop the project API.

### Packages
* [Pillow](https://pillow.readthedocs.io/en/stable/)
    * Used for image processing and validation.
* [asgiref](https://pypi.org/project/asgiref/)
    * A standard for Python asynchronous web apps and servers to communicate with each other.
* [dj-database-url](https://pypi.org/project/django-database-url/)
    * Used to parse the database URL in the production environment.
* [dj-rest-auth](https://pypi.org/project/dj-rest-auth/)
    * Used for handling authentication securely in the Django Rest Framework.
* [django-allauth](https://pypi.org/project/django-allauth/)
    * Used for the site's authentication system.
* [django-cors-headers](https://pypi.org/project/django-cors-headers/)
    * Used for cross-origin resource sharing (CORS) headers to responses.
* [django-filter](https://pypi.org/project/django-filter/)
    * Used to add queryset filtering.
* [djangorestframework-simplejwt](https://pypi.org/project/djangorestframework-simplejwt/)
    * A JSON Web Token authentication plugin for the Django REST Framework.
* [oauthlib](https://pypi.org/project/oauthlib/)
    * A framework that implements the logic of OAuth1 or OAuth2 without assuming a specific HTTP request object or web framework.
* [psycopg2](https://pypi.org/project/psycopg2/)
    * Used as a PostgreSQL database adapter for the Python programming language.
* [PyJWT](https://pypi.org/project/PyJWT/)
    * Used for encoding and decoding JSON Web Tokens.
* [python3-openid](https://pypi.org/project/python3-openid/)
    * OpenID support for modern servers and consumers.
* [pytz](https://pypi.org/project/pytz/)
    * Allows accurate and cross platform timezone calculations.
* [requests-oauthlib](https://pypi.org/project/requests-oauthlib/)
    * OAuthlib authentication support for Requests.
* [sqlparse](https://pypi.org/project/sqlparse/)
    * A non-validating SQL parser for Python.
* [django-allauth](https://pypi.org/project/django-allauth/)
    * Used for the site's authentication system.
* [gunicorn](https://pypi.org/project/gunicorn/)
    * A Python HTTP server for WSGI applications used to run the Python application concurrently.
* [django-cloudinary-storage](https://pypi.org/project/dj3-cloudinary-storage/)
    * Used to provide Cloudinary storages for media files as well as management commands for removing unnecessary files.

### Other Tools
* [Cloudinary](https://cloudinary.com/)
    * Used to store static files and media.
* [ElephantSQL](https://www.elephantsql.com/)
    * Used to host the database used in production.
* [GitHub](https://github.com/)
    * Used to store the repository.
* [Gitpod](https://www.gitpod.io/#get-started)
    * Used to create code/content and file structure for the respository.
* [Heroku](https://dashboard.heroku.com)
    * Used to host the deployed site.
