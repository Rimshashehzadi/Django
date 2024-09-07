# Django
1. Download Django from https://www.djangoproject.com/download
2. Installation of Django  'pip install django' run this comand in the computer terminal.
3. Check Django version 'py -m django --version' run this comand in the computer terminal.
4. Create first project in django  ' django-admin startproject projectname'
5. Change path go to the project using 'cd' comand.
6. Run server on the localhost: 'py manage.py runserver'
7. Now that the server’s running, visit http://127.0.0.1:8000/ with your web browser. You’ll see a “Congratulations!” page, with a rocket taking off. It worked!
8. Now that your environment – a “project” – is set up, you’re set to start doing work.Each application you write in Django consists of a Python package that follows a certain convention. Django comes with a utility that automatically generates the basic directory structure of an app, so you can focus on writing code rather than creating directories.
9. Projects vs. apps:

   What’s the difference between a project and an app? An app is a web application that does something – e.g., a blog system, a database of public records or a small poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects. 
10. To create your app, make sure you’re in the same directory as manage.py and type this command: 'py manage.py startapp polls'
11. Here mysite is a project and polls is an app.
12. Database Setup:
     Now, open up mysite/settings.py. It’s a normal Python module with module-level variables representing Django settings.

By default, the DATABASES configuration uses SQLite. If you’re new to databases, or you’re just interested in trying Django, this is the easiest choice. SQLite is included in Python, so you won’t need to install anything else to support your database. When starting your first real project, however, you may want to use a more scalable database like PostgreSQL, to avoid database-switching headaches down the road.

If you wish to use another database, see details to customize and get your database running.

While you’re editing mysite/settings.py, set TIME_ZONE to your time zone.

Also, note the INSTALLED_APPS setting at the top of the file. That holds the names of all Django applications that are activated in this Django instance. Apps can be used in multiple projects, and you can package and distribute them for use by others in their projects.

By default, INSTALLED_APPS contains the following apps, all of which come with Django:

. django.contrib.admin – The admin site. You’ll use it shortly.
. django.contrib.auth – An authentication system.
. django.contrib.contenttypes – A framework for content types.
. django.contrib.sessions – A session framework.
. django.contrib.messages – A messaging framework.
. django.contrib.staticfiles – A framework for managing static files.
These applications are included by default as a convenience for the common case.

Some of these applications make use of at least one database table, though, so we need to create the tables in the database before we can use them. To do that, run the following command:

 'py manage.py migrate'

 The migrate command looks at the INSTALLED_APPS setting and creates any necessary database tables according to the database settings in your mysite/settings.py file and the database migrations shipped with the app (we’ll cover those later). You’ll see a message for each migration it applies. If you’re interested, run the command-line client for your database and type \dt (PostgreSQL), SHOW TABLES; (MariaDB, MySQL), .tables (SQLite), or SELECT TABLE_NAME FROM USER_TABLES; (Oracle) to display the tables Django created.

Templates
Static
create superuser
Admin Login/Logout
MOdels
MoDELS AND  APP REGISTRATION
Database
Database Management
Crud(Continue)

