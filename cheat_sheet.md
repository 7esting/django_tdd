## 1.0 Cheat Sheet

Simple django app thanks to [Real Python](https://realpython.com/), it has been very useful to me for learning how to create my first Django app.  I will also use this app to learn how to deploy apps to the cloud. Using Ansible and later Jenkins.

Tasks
- [x] Setup Python virtual environment
- [x] Create Django procject
- [x] Create GitHub repository
- [x] Create Django app
- [ ] Setup backend database

Links:
* https://docs.djangoproject.com/en/2.1/intro/tutorial01/
* YouTube video crash course in Django (https://youtu.be/D6esTdOLXh4)

**Ensure that the system base Python installation is upto date**
```
python --version
python -m pip install --upgrade setuptools
python -m pip install --upgrade pip
```

**Create Python virtual environment inside the Project(s) root directory**
```
cd /path/to/src/django_tdd/
mkdir pyenv
cd pyenv
python -m venv /path/to/src/django_tdd/pyenv
```

Activate/Deactivate python virtual environment :
```
-Activate-
cd /path/to/src/django_tdd/
pyenv\Scripts\activate
-OR- in Linux
source pyenv/bin/activate
(pyenv) /path/to/src/django_tdd>

-Deactivate from any working directory-
deactivate
```

**Prepare virtual environment**
```
cd /path/to/src/
python –version
python -m pip --version
python -m pip install --upgrade setuptools
python -m pip install --upgrade pip
pip install django==2.1.7
pip install selenium==3.141.0

-Record pip modules installed in the virtual environment-
pip freeze > requirements.txt
```

**Start Contacts Django project and review the directory structure**

In the Django web framework what is Projects vs. apps

>What’s the difference between a project and an app? An app is a Web application that does something – e.g., a Weblog system, a database of public records or a simple poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.

>*https://docs.djangoproject.com/en/2.1/intro/tutorial01/*

Create the Django project [Project root dir /path/to/src/django_tdd]:
```
cd /path/to/src
mkdir django_tdd
cd django_tdd
django-admin startproject contacts
mkdir ft
cd ft
```

Create ft directory for functional test script(s) :
```
cd /path/to/src/django_tdd
mkdir ft
cd ft
```

Now create an app within the project:
```
cd user_contacts
```

Start the development server [port is optional] :
```
python manage.py runserver [8080]
```

**Manage Database Backend**

```
(pyenv) /path/to/src/django_tdd/contacts>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  No migrations to apply.
  Your models have changes that are not yet reflected in a migration, and so won't be applied.
  Run 'python manage.py makemigrations' to make new migrations, and then re-run 'python manage.py migrate' to apply them.
```

* python manage.py makemigrations    -- creates migration files based on your models
* python manage.py migrate     -- will create the tables in your db based on the migration files created
  (see docs for more details on database migrations)
* python manage.py createsuperuser    --will create a superuser for your application in the database (docs)


**Versioning: After creating the repo on GitHub**

Initialize the project root and add files to master repo :
```
cd /path/to/src/django_tdd
git help
git help <command>
git init
git add -A
```
Create a .gitignore file and add the files and directoires that should not be synched or pushed to GitHub
Also create a readme with markdown extension 'md' in wich the project is described.

Perform the first sync or commit with GitHub :
```
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/7esting/django_tdd.git
-OR- git remote add origin git@github.com:7esting/django_tdd.git
git push -u origin master
```

Check GitHub to verify the previous commit succeded and commit and push again :
```
git status
git commit -am "First commit"
git push
```

If push fails, check and set credentials on source host if needed. :
```
cd /path/to/src/django_tdd
git config -l
git config user.name ”7esting”
```
Show value of user.name use `git config user.name`

**Git Branching**

Show branches, create a new branch, and push to new branch :
```
git branch -a
git remote show origin
git checkout -b <name-of-new-branch>
git push --set-upstream <name-of-new-branch>
-OR-
git push origin <name-of-new-branch>
```

Switch to another branch :
```
git checkout -b <another-branch>
```

Merging \<other-branch\> with master branch.
Lets assume that we've been committing the latest changes to \<other-branch\>.
1. Switch to master branch
2. Merge \<other-branch\> with master
3. Add entire working directory/project root to master
4. Commit
5. Push to GitHub
```
git remote show origin
git checkout master
git merge <other-branch>
git add -A
git commit -am "Merged <other-branch> with master branch"
git push
git status
```

Deleting a branch :
```
git branch -d <name-of-branch>
```

**Fixing Untracked files (.gitignore) and Re-sync orgin with master**
```
git rm -r --cached .
git add -A
git commit -m "fixed untracked files"
git push
git status
```

---
## Django Project Directory Structure

Django Version 2.1.7

Django follows the MTV design pattern, where
* **Model:** Data access layer - Anythin to do with interacting, relating and validating the data.
* **Template:** Presentation layer - Presentation-related decisions
* **View:** Business logic layer - Accesses the model and displays the appropriate template

```
/path/to/src/django_tdd/pyenv/  <== Python virtual environment for Django
(env) /path/to/src/django_tdd/$ django-admin startproject contacts
(env) /path/to/src/django_tdd/$ python manage.py startapp user_contacts

/path/to/src/  <== Project(s) root directory
(pyenv) web@ubuntu:/path/to/src$
.
└── django_tdd  <== Project root directory
    ├── cheat_sheet.md
    ├── contacts  <== Django 'contacts' project root directory
    │   ├── contacts
    │   │   ├── __init__.py
    │   │   ├── settings.py
    │   │   ├── urls.py
    │   │   └── wsgi.py
    │   ├── db.sqlite3
    │   ├── ft  <== App directory (Functional Tests)
    │   │   ├── fixtures
    │   │   │   └── admin.json
    │   │   ├── ft_ut.json
    │   │   ├── __init__.py
    │   │   └── tests.py
    │   ├── manage.py
    │   └── user_contacts  <== App directory
    │       ├── admin.py
    │       ├── apps.py
    │       ├── __init__.py
    │       ├── migrations
    │       │   ├── 0001_initial.py
    │       │   ├── 0002_auto_20190307_1757.py
    │       │   └── __init__.py
    │       ├── models.py
    │       ├── new_contact_form.py
    │       ├── static
    │       │   └── images
    │       ├── templates
    │       │   ├── add.html
    │       │   ├── all.html
    │       │   ├── index.html
    │       │   └── layout.html
    │       ├── test_contact_form.py
    │       ├── tests.py
    │       ├── test_validator.py
    │       ├── test_views.py
    │       ├── urls.py
    │       ├── validators.py
    │       └── views.py
    ├── pyenv
    │   ├── bin
    │   │   ├── activate
    │   │   ├── activate.csh
    │   │   ├── activate.fish
    │   │   ├── django-admin
    │   │   ├── django-admin.py
    │   │   ├── easy_install
    │   │   ├── easy_install-3.6
    │   │   ├── pip
    │   │   ├── pip3
    │   │   ├── pip3.6
    │   │   ├── __pycache__
    │   │   │   └── django-admin.cpython-36.pyc
    │   │   ├── python -> python3
    │   │   └── python3 -> /usr/bin/python3
    │   ├── include
    │   ├── lib
    │   │   └── python3.6
    │   │       └── site-packages
    │   ├── lib64 -> lib
    │   ├── pyvenv.cfg
    │   └── share
    │       └── python-wheels
    │           ├── appdirs-1.4.3-py2.py3-none-any.whl
    │           ├── CacheControl-0.11.7-py2.py3-none-any.whl
    │           ├── certifi-2018.1.18-py2.py3-none-any.whl
    │           ├── chardet-3.0.4-py2.py3-none-any.whl
    │           ├── colorama-0.3.7-py2.py3-none-any.whl
    │           ├── distlib-0.2.6-py2.py3-none-any.whl
    │           ├── distro-1.0.1-py2.py3-none-any.whl
    │           ├── html5lib-0.999999999-py2.py3-none-any.whl
    │           ├── idna-2.6-py2.py3-none-any.whl
    │           ├── ipaddress-0.0.0-py2.py3-none-any.whl
    │           ├── lockfile-0.12.2-py2.py3-none-any.whl
    │           ├── packaging-17.1-py2.py3-none-any.whl
    │           ├── pip-9.0.1-py2.py3-none-any.whl
    │           ├── pkg_resources-0.0.0-py2.py3-none-any.whl
    │           ├── progress-1.2-py2.py3-none-any.whl
    │           ├── pyparsing-2.2.0-py2.py3-none-any.whl
    │           ├── requests-2.18.4-py2.py3-none-any.whl
    │           ├── retrying-1.3.3-py2.py3-none-any.whl
    │           ├── setuptools-39.0.1-py2.py3-none-any.whl
    │           ├── six-1.11.0-py2.py3-none-any.whl
    │           ├── urllib3-1.22-py2.py3-none-any.whl
    │           ├── webencodings-0.5-py2.py3-none-any.whl
    │           └── wheel-0.30.0-py2.py3-none-any.whl
    ├── README.md
    └── requirements.txt
```

##
:calendar:Last Updated on 6-MAR-2019