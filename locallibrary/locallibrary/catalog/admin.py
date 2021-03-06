from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language
# Register your models here.
# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Language)
# admin.site.register(BookInstance)

# @admin.register(Book) = admin.site.register(Book)

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
class BooksInline(admin.TabularInline):
    model = Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]
admin.site.register(Author, AuthorAdmin)
  

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    #直接在書下顯示bookInstance
    inlines = [BooksInstanceInline]

admin.site.register(Book, BookAdmin)

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {  # subtitle
            'fields': ('status', 'due_back', 'borrower')
        }),
    )


    