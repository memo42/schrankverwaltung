# Schrankverwaltung
This piece of Django code implements a basic warehouse management for crates of Mate and other beverages.

## HTPASSWD
* OPTIONAL
* needs to be reflected in apache configuration
* needs a htpasswd file readable for the webservers user in /etc/schrankverwaltung/.htpasswd 
* Format: user:password
## Secure Key
* needs a settings.ini in schrank/schrankverwaltung/settings.ini
* Format: [secrets]\nSECRET_KEY: "$secret_key"
## Initialize database
* run python manage.py syncdb
* open ?/main/
* to create link between overview cupboard and individual cupboard use admin interface
