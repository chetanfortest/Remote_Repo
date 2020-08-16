from django.contrib import admin
from testapp.models import Movies

# Register your models here.

class MoviesAdmin(admin.ModelAdmin):
	list_display = ['name', 'language']

admin.site.register(Movies,MoviesAdmin)
