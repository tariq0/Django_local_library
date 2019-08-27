from django.contrib import admin
from .models import Genre, Language, Author, Book, Book_Instance

# Register your models here.

admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Book_Instance)
