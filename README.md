# akb #

## Deploying the app ##
Short instructions for deploying the application.
The initial solution is to use apache httpd with mod_wsgi, as recommended by the django documentation.
The final production enviroment is still unclear(, f.e nginx with uWSGI would be another option).

Source:
- [Django's How-to](https://docs.djangoproject.com/en/1.11/howto/deployment/)
- [Introduction to mod_wsgi-express](http://blog.dscpl.com.au/2015/04/introducing-modwsgi-express.html)

### Installation of mod_wsgi ###
We use the python installer pip, to get our mod_wsgi and evtl httpd running.
We install the modul with `pip3 install mod_wsgi` in the existing python installation, further information
can be found at ['Introduction to mod_wsgi-express'](http://blog.dscpl.com.au/2015/04/introducing-modwsgi-express.html).

### The deployment directory ##
/usr/local/www:
  - /static/ : for static files (with `manage.py collectstatic`)
  - ...

