from django.contrib import admin
from .models import Author, Genre, Book, BookInstance

# Register your models here.
# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)
class BookInstanceInline(admin.TabularInline):
	model = BookInstance

class BookInline(admin.TabularInline):
	model  = Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
	fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
	inlines = [BookInline]

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'display_genre')
	inlines = [BookInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
	list_filter = ('status', 'due_back')
	list_display = ('id', 'status', 'due_back')
	
	fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )