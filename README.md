Conductoor API
==============

Requirements
------------
`Python 3.4`

Running the application
-----------------------

Installing the requirements:
`pip install -r requirements.txt`

Loading the provided initial data
`python3 manage.py loaddata fixtures/initial_data.yaml`

Running the application:
`python3 manage.py runserver`

Other
-----

Destroying the database and loading the initial data in Heroku:  
`heroku pg:reset DATABASE_URL`
`heroku run python3 manage.py syncdb` (answer no for superuser)
`python3 manage.py loaddata fixtures/initial_data.yaml`
