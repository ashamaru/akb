# About #
akb_base was initialized with "django-admin startproject akb_base".


# usefull commands... #
-- for all of these commands you need to be in the directory with "manage.py" in it --
for further information vistit [this](https://docs.djangoproject.com/en/1.11/)
## ... general ##
python3 manage.py runserver 	--> starts the developement server (strg+c shuts it down)
python3 manage.py startapp app_name	--> initializes the app app_name (creates necessary files)

## ... for Database ##
python3 manage.py migrate 	--> migrates the database according to settings.py, applies migrations
python3 manage.py makemigrations app_name	--> run this if you changed your models in app_name


to be continued...


 
