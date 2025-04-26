from django.contrib import admin
from .models import Article
from .admin_sites import editor_admin, publisher_admin, archive_admin

# Базовый класс ModelAdmin с общей конфигурацией
class BaseArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'author', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'content')
    readonly_fields = ('created_at', 'updated_at')
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(author=request.user)
        return qs

# Специализированные классы для разных админок
class EditorArticleAdmin(BaseArticleAdmin):
    fields = ('title', 'content', 'status')
    list_editable = ('status',)
    actions = ['make_draft']
    
    def make_draft(self, request, queryset):
        queryset.update(status='draft')
    make_draft.short_description = "Перевести выбранные статьи в черновики"

class PublisherArticleAdmin(BaseArticleAdmin):
    fields = ('title', 'content', 'status')
    list_editable = ('status',)
    actions = ['publish_articles']
    
    def publish_articles(self, request, queryset):
        queryset.update(status='published')
    publish_articles.short_description = "Опубликовать выбранные статьи"
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.exclude(status='archived')

class ArchiveArticleAdmin(BaseArticleAdmin):
    fields = ('title', 'content', 'status')
    actions = ['archive_articles']
    
    def archive_articles(self, request, queryset):
        queryset.update(status='archived')
    archive_articles.short_description = "Перевести выбранные статьи в архив"
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.exclude(status='draft')

# Регистрация моделей в разных админках
editor_admin.register(Article, EditorArticleAdmin)
publisher_admin.register(Article, PublisherArticleAdmin)
archive_admin.register(Article, ArchiveArticleAdmin)

# Опционально: регистрация в стандартной админке
admin.site.register(Article, BaseArticleAdmin)