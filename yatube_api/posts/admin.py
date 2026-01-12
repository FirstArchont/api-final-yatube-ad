from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Post, Group, Comment, Follow


User = get_user_model()


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description_short')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'description')
    fields = ('title', 'slug', 'description')

    @admin.display(description='Описание (кратко)')
    def description_short(self, obj):
        return (
            obj.description[:50]
            + '...' if len(obj.description) > 50 else obj.description)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text_short', 'author', 'pub_date', 'group')
    list_filter = ('pub_date', 'author', 'group')
    search_fields = ('text',)
    date_hierarchy = 'pub_date'
    raw_id_fields = ('author', 'group')
    fields = ('author', 'text', 'group', 'image', 'pub_date')
    readonly_fields = ('pub_date',)

    @admin.display(description='Текст (кратко)')
    def text_short(self, obj):
        return obj.text[:50] + '...' if len(obj.text) > 50 else obj.text


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text_short', 'author', 'post', 'created')
    list_filter = ('created', 'author', 'post__author')
    search_fields = ('text', 'author__username', 'post__text')
    raw_id_fields = ('author', 'post')
    fields = ('author', 'post', 'text', 'created')
    readonly_fields = ('created',)

    @admin.display(description='Комментарий (кратко)')
    def text_short(self, obj):
        return obj.text[:50] + '...' if len(obj.text) > 50 else obj.text


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'following')
    list_filter = ('user', 'following')
    search_fields = ('user__username', 'following__username')
    raw_id_fields = ('user', 'following')
