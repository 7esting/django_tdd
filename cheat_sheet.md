## 1.0 Cheat Sheet

Preparege a python virtual environment and create a simple django app.

Tasks
- [x] Setup Python virtual environment
- [x] Create Django procject
- [x] Create GitHub repository
- [ ] Create Django app
- [ ] Setup backend database

Usefull links:
* https://docs.djangoproject.com/en/2.1/intro/tutorial01/
* YouTube video crash course in Django (https://youtu.be/D6esTdOLXh4)

**Ensure that the system base Python installation is upto date**
```
python --version
python -m pip install --upgrade setuptools
python -m pip install --upgrade pip
```

**Create Python virtual environment**
```
cd /path/to/django_tdd/
mkdir django_tdd_pyenv
cd django_tdd_pyenv
python -m venv /path/to/django_tdd/django_tdd_pyenv
Scripts\activate
```
To close environment type :
```
(pyenv) /path/to/django_tdd> deactivate
```

**Prepare virtual environment**
```
python –version
python -m pip --version
python -m pip install --upgrade setuptools
python -m pip install --upgrade pip
pip install django==2.1.7
pip install selenium==3.141.0
```

**Start Contacts Django project and review the directory structure**

In the Django framework what is Projects vs. apps

#####What’s the difference between a project and an app? An app is a Web application that does something – e.g., a Weblog system, a database of public records or a simple poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.

#####https://docs.djangoproject.com/en/2.1/intro/tutorial01/

Create the Django project :
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
python manage.py startapp user_contacts
```

Start the development server [port is optional] :
```
python manage.py runserver [8080]
```

* python manage.py makemigrations    -- creates migration files based on your models
* python manage.py migrate     -- will create the tables in your db based on the migration files created
  (see docs for more details on database migrations)
* python manage.py createsuperuser    --will create a superuser for your application in the database (docs)


**Versioning: After creating the repo on GitHub**

Initialize the project root and add files to master repo :
```
cd /path/to/django_tdd
git init
git add .
```
Create a .gitignore file and add the files and directoires that should not be synched or pushed to GitHub
Also create a readme with markdown extension 'md' in wich the project is described.

Perform the first sync or commit with GitHub :
```
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/7esting/django_tdd.git
-Or git remote add origin git@github.com:7esting/django_tdd.git
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
cd /path/to/django_tdd
git config -l
git config user.name ”7esting”
```
Show value of user.name :
```
git config user.name
```
**Git Branching**

Show branches, create a new branch, and push to new branch :
```
git branch
git checkout -b <name-of-new-branch>
git push --set-upstream <name-of-new-branch>
```

Merging with master branch :


Deleting a branch :
```
git branch -d <name-of-new-branch>
```



**Fixing Untracked files (.gitignore) and Re-sync orgin with master**
```
git rm -r --cached .
git add .
git commit -m "fixed untracked files"
git push
git status
```
##

:calendar:Last Updated on 6-MAR-2019