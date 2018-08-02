
# Linux Server Configuration

This is the final project of the Udacity course:  Full Stack Web Developer


## Information Details:
* URL for access - http://ec2-35-182-221-65.ca-central-1.compute.amazonaws.com
* Local IP Address - http://35.182.221.65
* SSH port- 2200
* Login with : ssh grader@35.182.221.65 -p 2200 -i ~/.ssh/grader
* Password: grader

### Software installed
Web server has been configured to serve the Item Catalog application as a WSGI app


### Configurations made
* Created a new user named grader
* Give grade user sudo permition
* Update all currently installed packages
* Changed the SSH port from 22 to 2200
* Generated key-pair with ssh-keygen for grade user
* Configured the Uncomplicated Firewall (UFW) to only allow incoming connections for SSH (port 2200), HTTP (port 80), and NTP (port 123)
* Configured the local timezone to UTC
* Installed and configure Apache to serve a Python mod_wsgi application
* Install Git
* Deploy Flask Application
* Install Postgresql

### Third-party resources
* Sudo instalations (sudo apt-get install)
```
update
upgrade
apache2
libapache2-mod-wsgi
git
python-pip
python-psycopg2
postgresql postgresql-contrib

```

* Pip instalations (sudo pip install)
```
Flask
httplib2
requests
--upgrade oauth2client
sqlalchemy
Flask-SQLAlchemy
flask-seasurf

```

## Run linux server

After login in the machine via ssh, go to the catalog foler
```
cd /var/www/catalog/catalog/
```
Run the following command
```
python __init__.py
```
