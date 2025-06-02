from django.contrib import admin
# from todo import models
from todo.models import TodoItem as Todo    
admin.site.register(Todo)