from django.contrib import admin
from .models import Account, Post


class PostInline(admin.TabularInline):
    model = Post
    fields = ['title', 'brief_text']

    # No adding and no change
    def has_add_permission(self, request, obj):
        return False

    def has_change_permission(self, request, obj=None):
        return False


class AccountAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'city', 'posts_amount']
    search_fields = ['first_name', 'last_name']
    fields = ['first_name', 'last_name', 'city', 'birth_date', 'posts_amount']
    inlines = [PostInline]

    def posts_amount(self, obj):
        return obj.posts.count()

    def has_change_permission(self, request, obj=None):
        return False


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'brief_text', 'author_name', 'likes_amount', 'comments_amount']
    list_filter = ['author']
    search_fields = ['title']
    fields = ['title', 'full_text', 'main_picture', 'author_name', 'likes_amount',
              'comments_amount']
    readonly_fields = ['author_name', 'likes_amount', 'comments_amount']

    def likes_amount(self, obj):
        return obj.likes.count()

    def comments_amount(self, obj):
        return obj.comments.count()

    def author_name(self, obj):
        return obj.author.get_full_name()

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Account, AccountAdmin)
admin.site.register(Post, PostAdmin)