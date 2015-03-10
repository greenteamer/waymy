# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple
from image_cropping import ImageCroppingMixin
from django.utils.translation import ugettext_lazy as _

from webshop.catalog.forms import ProductAdminForm
from webshop.catalog.models import *

from mptt_tree_editor.admin import TreeEditor

# from suit import


# class CharacteristicAdmin(admin.StackedInline):
#     """Добавление характеристик для продуктов"""
#     model = Characteristic
#     extra = 1
#     fieldsets = [
#         (_(u'Characteristic'), {'fields': ['characteristic_type']}),
#         (_(u'Value'), {'fields': ['value']}),
#     ]


class ProductImageAdmin(ImageCroppingMixin, admin.StackedInline):
    """Добавление изображений продукта"""
    model = ProductImage
    exclude = ('description',)
    extra = 0
    # fieldsets = [
    #     (_(u'Image'), {'fields': ['image']}),
    #     # (_(u'Description'), {'fields': ['description']}),
    #     (_(u'Default'), {'fields': ['default']}),
    # ]

class ProductVolumeAdmin(admin.StackedInline):
    """Добавление изображений продукта"""
    model = ProductVolume
    extra = 0


class ProductAdmin(ImageCroppingMixin, admin.ModelAdmin):
    """
    Управление товарами
    Как будут отображаться поля товаров в разделе администрирования
    """
    form = ProductAdminForm
    list_display = ('id', 'name', 'created_at', 'updated_at')
    list_display_links = ('name',)
    list_per_page = 50
    ordering = ['-created_at']
    inlines = [ProductVolumeAdmin, ProductImageAdmin]
    # search_field = ['name', 'description', 'meta_keywords', 'meta_description']
    search_fields = ['name']
    # exclude = ('meta_keywords', 'meta_description')
    readonly_fields = ('created_at', 'updated_at',)
    # имя продукта для генерации чистой ссылки
    prepopulated_fields = {'slug': ('name',)}
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }


class CategoryAdmin(TreeEditor):
    """
    Управление категориями
    Как будут отображаться поля категорий в разделе администрирования
    """
    list_display = ("indented_short_title", "actions_column", 'name', 'created_at', 'updated_at',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['created_at']
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    readonly_fields = ('created_at', 'updated_at',)
    # exclude = ('created_at', 'updated_at',)
    prepopulated_fields = {'slug': ('name',)}

# class BrandNameAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#     list_display_links = ('name',)
#     ordering = ['name']
#     search_fields = ['name']

class FeelNameAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    ordering = ['name']
    search_fields = ['name']

# class GiftPriceAdmin(admin.ModelAdmin):
#     list_display = ('price',)
#     list_display_links = ('price',)
#     search_fields = ['price']


# Регистрирация моделей в админке
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(BrandName)
# admin.site.register(FeelName, FeelNameAdmin)
admin.site.register(GiftPrice)
admin.site.register(Cupon)
admin.site.register(Review)
# admin.site.register(CharacteristicType)
