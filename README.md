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

 