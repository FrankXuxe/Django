'''
Request: When people put in an URL to load the web page
get request: get the information from the database, flow from database to application server to webserver to webpage
psot request: send information to the database so it can post it, flows backward 

Django is a server-side web framework that encompasses all the elements that can help build interactive website
Learing log: an online journal to let you keep track of what you have learned

Models: models.py: define all the tables, 
view.py: python to interact with application server, 
urls.py: the actual url of webpage, 
templates: webpage and wesbserber

pip install -r requirements.txt
django-admin startproject learning_log .
py manage.py migrates
py manage.py runserver
py manage.py startapp MainApp
-m pip install -U autopep8
py manage.py makemigrations
py manage.py migrate
py manage.py createsuperuser
'''