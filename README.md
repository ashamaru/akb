# akb #

## Deploying the app ##
Short instructions for deploying the application.
The initial solution is to use apache httpd with mod_wsgi, as recommended by the django documentation.
The final production environment is still unclear(, f.e nginx with uWSGI would be another option).

Source:
- [Django's How-to](https://docs.djangoproject.com/en/1.11/howto/deployment/)
- [Introduction to mod_wsgi-express](http://blog.dscpl.com.au/2015/04/introducing-modwsgi-express.html)

### Installation of mod_wsgi ###
We use the python installer pip, to get our mod_wsgi and evtl httpd running.
Optionally install apache2 with `pip3 install mod_wsgi-httpd` before.
We install the modul with `pip3 install mod_wsgi` in the existing python installation, further information
can be found at ['Introduction to mod_wsgi-express'](http://blog.dscpl.com.au/2015/04/introducing-modwsgi-express.html).

### The deployment directory ###
The directory choice is up to the admin, but f.e.
/usr/local/www/static/ : for static files (with `manage.py collectstatic`)
and another directory for the app. It might be a good consideration not to put the app in the same directory
hierarchy like the statics, to avoid accidently serving code.

### Using collectstatic ###
Simply add the variable STATIC_ROOT with the absolut path to the target directory to your settings.py, f.e.`STATIC_ROOT = '/usr/local/www/static/'`. After that, `python3 manage.py collectstatic` will push the project's static files to the directory which STATIC_ROOT points to. If there were changes to your static project files, simply run the command again.

### Starting up the server ###
The command:
```bash
mod_wsgi-express start-server --url-alias /static /path/to/static_directory --working-directory /path/to/projectdirectory
/path/to/wsgi_executable
```
For `--url-alias`, don't use trailing backslashes, f.e. use `/static /usr/local/www/static`.
`--working-directory` is the directory with manage.py in it.
The error log directory will be outputted by the command, or use --log-to-terminal for convenience.
The last argument is the module with application callable in it. In django, it's wsgi.py, in the directory with settings.
For further information, use mod_wsgi-express [subcommand] -h|--help or simply refer to documentation online.



