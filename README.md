# insightjedi
Sample Django application to provide create, put, post, delete and list request methods over a Document model.

Setup -
1. Create virtual environment with Python 3+ version. This application is developed over Python 3.7.6 version, please upgrade in case of descrepencies.
2. pip install dependencies from requirements.txt.
3. Connect with database PostgreSQL after creating database 'insightjedi' from shell and update USERNAME and PASSWORD in settings.py
4. Users which are linked to Document model as well, are needed to be created through Admin Panel, 'localhost:PORT/admin'. To access Admin Panel, please create super user using 'python manage.py createsuperuser' within the project.
