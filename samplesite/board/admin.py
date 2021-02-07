from django.contrib import admin
from .models import Board, Rubric, AdditionalImage

# Register your models here.


class AdditionalImageInline(admin.TabularInline):
    model = AdditionalImage


class BoardAdmin(admin.ModelAdmin):
    inlines = [AdditionalImageInline, ]
    list_display = ('user', 'title', 'image', 'content', 'price', 'published', 'contacts', 'rubric', 'is_active')
    fields = (('rubric', 'user'), 'title', 'content', 'price', 'contacts', 'image', 'is_active')

    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')


admin.site.register(Board, BoardAdmin)
admin.site.register(Rubric)
