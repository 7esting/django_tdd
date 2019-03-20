<<<<<<< HEAD
## Manually deploying the app to a local machine 

Setup djanjo_tdd project app on an instance running Ubuntu

Create OS user
```
adduser web-admin
id web-admin
uid=1004(web-admin) gid=1008(web-admin) groups=1008(web-admin)
ansinode@ubuntu:~$ sudo vi /etc/sudoers
#web-admin ALL=(ALL) NOPASSWD: ALL
```

**Clone GitHub django_tdd repo to /home/web-admin/src/**

1. Login as web-admin user `sudo su - web-admin` and create src directory
```
cd /home/web-admin/
mkdir src
cd src
```

2. Generate ssh keys and use default name for keys
```
ssh-keygen -t rsa -b 4096 -C 7esting@gmail.com
```

3. Add public key to github.com/7esting/django_tdd and don't allow write access
```
# Quit test
ssh git@github.com
PTY allocation request failed on channel 0
Hi 7esting/django_tdd! You've successfully authenticated, but GitHub does not provide shell access.
Connection to github.com closed.
# Clone repo
git clone ssh://git@github.com/7esting/django_tdd.git
cd django_tdd
git status
```

**Create python virtual environment inside the Django project root**
```
python3 --version
sudo apt-get install python3-venv
cd /home/web-admin/src/django_tdd
mkdir pyenv
python3 -m venv ./pyenv
source pyenv/bin/activate
python3 -m pip install -r requirements.txt
```

**Setup Nginx with out ssl and make sure web app works**
```
(pyenv) web-admin@ubuntu:~/src/django_tdd/contacts$ python manage.py runserver
# From a different session on Ubuntu open url to app
elinks http://127.0.0.1:8000/
```

Configure Nginx with SSL & WSGI with Django app 
- Use Self-Signed SSL
- check Nginx configuration `nginx -t`

Setup a Linux systemd startup service to manage long running processe like ***gunicorn***
*You can run **gunicorn** as a socket, but I had issues with running it as a socket for some reason.*

*Python's WSGI application server [gunicorn](https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/gunicorn/)*
```
root@ubuntu:/etc/systemd/system# vi gunicorn_tcp.service 
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=web-admin
Group=web-admin
WorkingDirectory=/home/web-admin/src/django_tdd/contacts
ExecStart=/home/web-admin/src/django_tdd/pyenv/bin/gunicorn --access-logfile - --workers 3 --bind 127.0.0.1:8000 contacts.wsgi

[Install]
WantedBy=multi-user.target
### EOF
```

Enable ***gunicorn_tcp*** service
```
root@ubuntu:/etc/systemd/system# systemctl enable gunicorn_tcp
Created symlink /etc/systemd/system/multi-user.target.wants/gunicorn_tcp.service → /etc/systemd/system/gunicorn_tcp.service.
root@ubuntu:/etc/systemd/system# systemctl is-enabled gunicorn_tcp
enabled
```

In the Django project settings.py add the IPs or DNS names on which the application will respond.  To avoid error:
`Invalid HTTP_HOST header: '192.168.56.1'. You may need to add '192.168.56.1' to ALLOWED_HOSTS.`
```
vi /home/web-admin/src/django_tdd/contacts/contacts
ALLOWED_HOSTS = ['127.0.0.1', 192.168.56.1', 'hector.ddns.info']
```

Update Ubuntu firewall
```
ufw status
ufw app list
ufw app info 'Nginx Full'
    Profile: Nginx Full
    Title: Web Server (Nginx, HTTP + HTTPS)
    Description: Small, but very powerful and efficient web server

    Ports:
    80,443/tcp
ufw allow 'Nginx Full'
ufw status
```

Update Nginx **sites-enabled**
```
root@ubuntu:/etc/nginx/sites-enabled# ln -s /etc/nginx/conf.d/contacts.conf contacts
root@ubuntu:/etc/nginx/sites-enabled# nginx -t
nginx: [warn] "ssl_stapling" ignored, issuer certificate not found for certificate "/etc/ssl/certs/ssl-cert-snakeoil.pem"
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

**Changing the backend database from db.sqlite to PostgreSQL**

*Django supports PostgreSQL 9.4 and higher. psycopg2 2.5.4 or higher is required, though the latest release is recommended.* [https://docs.djangoproject.com/en/2.1/ref/databases/]

1. Install any python module(s) necessary
Activate Python virtual environment first then `pip install psycopg2`

Or if yo downloaded the package locally
```
python setup.py build
sudo python setup.py install
```
2. Update the DATABASES setting in [Django's settings.py]([https://docs.djangoproject.com/en/2.1/ref/settings/)
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

## Showing Static content

Gunicorn only serves up dynamic content, so Django and Nginx needs to be configured to serve static content, such as images, css and js.

*Add or edit STATICFILES_DIRS in settings.py*
```
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
```

Run the following command to generate admin static files in static_dirs location
```
python manage.py collectstatic
```

**Nginx static content settings**
```
# nginx serve up static files, not through WSGI server
    #location ^/static.* {
    location /static {
        autoindex on;
        alias /home/web-admin/src/django_tdd/contacts/static;
    }
```
##

=======
## Manually deploying the app to a local machine 

Setup djanjo_tdd project app on an instance running Ubuntu

Create OS user
```
adduser web-admin
id web-admin
uid=1004(web-admin) gid=1008(web-admin) groups=1008(web-admin)
ansinode@ubuntu:~$ sudo vi /etc/sudoers
#web-admin ALL=(ALL) NOPASSWD: ALL
```

**Clone GitHub django_tdd repo to /home/web-admin/src/**

1. Login as web-admin user `sudo su - web-admin` and create src directory
```
cd /home/web-admin/
mkdir src
cd src
```

2. Generate ssh keys and use default name for keys
```
ssh-keygen -t rsa -b 4096 -C 7esting@gmail.com
```

3. Add public key to github.com/7esting/django_tdd and don't allow write access
```
# Quit test
ssh git@github.com
PTY allocation request failed on channel 0
Hi 7esting/django_tdd! You've successfully authenticated, but GitHub does not provide shell access.
Connection to github.com closed.
# Clone repo
git clone ssh://git@github.com/7esting/django_tdd.git
cd django_tdd
git status
```

**Create python virtual environment inside the Django project root**
```
python3 --version
sudo apt-get install python3-venv
cd /home/web-admin/src/django_tdd
mkdir pyenv
python3 -m venv ./pyenv
source pyenv/bin/activate
python3 -m pip install -r requirements.txt
```

**Setup Nginx with out ssl and make sure web app works**
```
(pyenv) web-admin@ubuntu:~/src/django_tdd/contacts$ python manage.py runserver
# From a different session on Ubuntu open url to app
elinks http://127.0.0.1:8000/
```

Configure Nginx with SSL & WSGI with Django app 
- Use Self-Signed SSL
- check Nginx configuration `nginx -t`

Setup a Linux systemd startup service to manage long running processe like ***gunicorn***
*You can run **gunicorn** as a socket, but I had issues with running it as a socket for some reason.*

*Python's WSGI application server [gunicorn](https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/gunicorn/)*
```
root@ubuntu:/etc/systemd/system# vi gunicorn_tcp.service 
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=web-admin
Group=web-admin
WorkingDirectory=/home/web-admin/src/django_tdd/contacts
ExecStart=/home/web-admin/src/django_tdd/pyenv/bin/gunicorn --access-logfile - --workers 3 --bind 127.0.0.1:8000 contacts.wsgi

[Install]
WantedBy=multi-user.target
### EOF
```

Enable ***gunicorn_tcp*** service
```
root@ubuntu:/etc/systemd/system# systemctl enable gunicorn_tcp
Created symlink /etc/systemd/system/multi-user.target.wants/gunicorn_tcp.service → /etc/systemd/system/gunicorn_tcp.service.
root@ubuntu:/etc/systemd/system# systemctl is-enabled gunicorn_tcp
enabled
```

In the Django project settings.py add the IPs or DNS names on which the application will respond.  To avoid error:
`Invalid HTTP_HOST header: '192.168.56.1'. You may need to add '192.168.56.1' to ALLOWED_HOSTS.`
```
vi /home/web-admin/src/django_tdd/contacts/contacts
ALLOWED_HOSTS = ['127.0.0.1', 192.168.56.1', 'hector.ddns.info']
```

Update Ubuntu firewall
```
ufw status
ufw app list
ufw app info 'Nginx Full'
    Profile: Nginx Full
    Title: Web Server (Nginx, HTTP + HTTPS)
    Description: Small, but very powerful and efficient web server

    Ports:
    80,443/tcp
ufw allow 'Nginx Full'
ufw status
```

Update Nginx **sites-enabled**
```
root@ubuntu:/etc/nginx/sites-enabled# ln -s /etc/nginx/conf.d/contacts.conf contacts
root@ubuntu:/etc/nginx/sites-enabled# nginx -t
nginx: [warn] "ssl_stapling" ignored, issuer certificate not found for certificate "/etc/ssl/certs/ssl-cert-snakeoil.pem"
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

**Changing the backend database from db.sqlite to PostgreSQL**

*Django supports PostgreSQL 9.4 and higher. psycopg2 2.5.4 or higher is required, though the latest release is recommended.* [https://docs.djangoproject.com/en/2.1/ref/databases/]

1. Install any python module(s) necessary
Activate Python virtual environment first then `pip install psycopg2`

Or if yo downloaded the package locally
```
python setup.py build
sudo python setup.py install
```
2. Update the DATABASES setting in [Django's settings.py]([https://docs.djangoproject.com/en/2.1/ref/settings/)
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

## Showing Static content

Gunicorn only serves up dynamic content, so Django and Nginx needs to be configured to serve static content, such as images, css and js.

*Add or edit STATICFILES_DIRS in settings.py*
```
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
```

Run the following command to generate admin static files in static_dirs location
```
python manage.py collectstatic
```

**Nginx static content settings**
```
# nginx serve up static files, not through WSGI server
    #location ^/static.* {
    location /static {
        autoindex on;
        alias /home/web-admin/src/django_tdd/contacts/static;
    }
```
##

>>>>>>> linux-version
