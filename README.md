#### Start local server: python manage.py runserver
#### Start a new app: python manage.py startapp products
#### Show migrations: python manage.py showmigrations
#### Looks at models and determines what changes we need to do in the database to match our models: python manage.py makemigrations
#### Show the SQL we are running: python manage.py sqlmigrate products 0001
#### Run migrations: python manage.py migrate
#### Create admin user: python manage.py createsuperuser