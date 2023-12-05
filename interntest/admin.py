from django.contrib import admin

from interntest.models import Product, Comment


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
