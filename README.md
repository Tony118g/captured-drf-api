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

## Deployment and Development
* The project API was developed using [Gitpod](https://www.gitpod.io/#get-started) to create the code and overall file structure.
* [GitHub](https://github.com/) is used to host the repository.

### Deployment
This project API was deployed using [Heroku](https://id.heroku.com/login).

NB - to ensure a successful deployment of the project in Heroku, you need to ensure that you create a Procfile and a requirements.txt file.

Once you are certain that everything is ready to deploy the reposotry, you can go throught the following steps to do so:

1. Log in to Heroku or create an account if necessary.
2. Click on the button labeled "New" from the dashboard in the top right corner and select the "Create new app" option in the drop-down menu.
3. Enter a unique name for the application and select the region you are in.
    * For this API, the unique name is "captured-drf-api" and the region selected is Europe.
4. Click on "create app".
5. Navigate to the settings tab and click "Reveal config vars".
6. Add the necessary config vars for the project.
7. Navigate to the "Deploy".
8. Select "GitHub" as the deployment method and click "Connect to GitHub".
9. Search for the GitHub repository that you wish to deploy and click on "connect" to link the repository to Heroku.
10. Scroll down and click on "Deploy Branch" to manually deploy.
11. Once the app has deployed successfully, Heroku will notify you and provide a button to view the app.

NB - If you wish to rebuild the deployed app automatically every time you push to GitHub, you may click on "Enable Automatic Deploys" in Heroku.

### Forking the Repository
To copy the repository for viewing and editing without affecting the original version you can fork the repository using the following steps:

1. In the "captured-drf-api" repository, click on the "fork" tab in the top right corner.
2. Click on "create fork" to fork the repository in your own GitHub account.

### Cloning The Repository
To clone the repository through GitHub, follow these steps:

1. In the repository, select the "code" tab located at the top of the list of files.
2. Ensure "HTTPS" is selected in the dropdown menu.
3. Copy the URL under HTTPS.
4. Open Git Bash in your IDE of choice.
5. Change the working directory to the location where you want the cloned directory to be created.
6. Type "git clone" and paste the URL that was copied from the repository.
7. Press "enter" to create the clone.

### The ElephantSQL Database
[ElephantSQL](https://www.elephantsql.com/) is used to host the database for this project in production. The process to set this up is as follows:

1. Sign up or log in to ElephantSQL with your GitHub account.
2. Click on "Create New Instance".
3. Enter a name for the instance.
4. Select the "Tiny Turtle (Free)" free plan.
5. The "Tags" field can be left blank.
6. Click "Select Region".
7. Select an appropriate data center near you.
8. Click "Review".
9. Ensure that all details are correct and then click "Create instance".
10. Once created, you can return to the dashboard and click on the relevant instance to view details such as the database URL and password.

### The Cloudinary API
[Cloudinary](https://cloudinary.com/) is used in this project to store media assets and static files. This is done because Heroku does not provide reliable and suitable media file storage.

To set up Cloudinary, follow these steps:

1. Login/sign up to Cloudinary.
2. Navigate to the dashboard to view the API Environment Variable.

NB - You are able but not required to change your assigned cloud name to something more memorable.