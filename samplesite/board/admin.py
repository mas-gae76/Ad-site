from django.contrib import admin
from .models import Board, Rubric

# Register your models here.


class BoardAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'content', 'price', 'published', 'rubric')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')


admin.site.register(Board, BoardAdmin)
admin.site.register(Rubric)
