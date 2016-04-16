# Schrankverwaltung
This piece of Django code implements a basic warehouse management for crates of Mate and other beverages.

### HTPASSWD
* OPTIONAL
* needs to be reflected in apache configuration
* needs a htpasswd file readable for the webservers user in /etc/schrankverwaltung/.htpasswd
* Format: user:password

### Secure Key
* needs a settings.ini in /etc/schrankverwaltung/settings.ini
* Format: [secrets]\nSECRET_KEY: "$secret_key"

### Initialize database
* run python manage.py syncdb
* open ?/main/
* to create link between overview cupboard and individual cupboard use admin interface

# HowTo use
on a linux system with screen installed simply execute the starttestserver script

then go to localhost:8000/main

To visit the overview of the cupboard in a room go to localhost:8000/main/Roomnumber
The link between a cupboard and the room it is in must be set manually in the current version (can be done in the admin interface)
e.g. localhost:8000/main/E304

To visit the page of a specific locker go to localhost:8000/main/roomnumber.cupboardnumber where cupboardnumber is between 1 and the number of cupboarddoors in that room.
e.g. localhost:8000/main/E304.1

To get a admin view over the database go to
localhost:8000/admin
The user and password are the ones specified when initializing the database.
