from django.contrib import admin
from .models import Category, Post

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published', 'post_categories')
    ordering = ('author', 'published')
    # Buscador
    search_fields = ('title', 'content', 'author__username', 'categories__name')
    # filtro por fechas
    date_hierarchy = 'published'
    # lista de filtro 
    list_filter = ('author__username', 'categories__name')

    def post_categories(self, obj):
        return ', '.join(obj.categories.all().order_by('name').values_list('name', flat=True))
    
    post_categories.short_description = 'Categorias'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)