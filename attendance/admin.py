from django.contrib import admin
from .models import Book, Student

# Register your models here.
# admin.site.register(Book)
# admin.site.register(Student)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # list_per_page = 2
    # list_editable = ['isbn']
    list_display = ['title', 'no_of_pages', 'isbn']
    list_filter = ['date']
    search_fields = ['title', 'body', 'author']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'track', 'mentor']
    search_fields = ['mentor', 'goals', 'track']
