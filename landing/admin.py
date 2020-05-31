from django.contrib import admin
from suit.sortables import SortableTabularInline, SortableModelAdmin

from .models import (
    Menu, Promo, Size, Trending, Status,
    Category, Product, Testimonial, Blog,
    Feature
)


@admin.register(Menu)
class MenuAdmin(SortableModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)

    sortable = 'id'


@admin.register(Promo)
class PromoAdmin(SortableModelAdmin):
    search_fields = ('caption',)
    list_display = ('caption',)
    sortable = 'id'


@admin.register(Trending)
class TrendingAdmin(SortableModelAdmin):
    search_fields = ('headline',)
    list_display = ('headline',)
    sortable = 'id'


@admin.register(Product)
class ProductAdmin(SortableModelAdmin):
    search_fields = ('title',)
    list_display = ('title',)
    sortable = 'id'


@admin.register(Size)
class SizeAdmin(SortableModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)
    sortable = 'id'


@admin.register(Status)
class StatusAdmin(SortableModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)
    sortable = 'id'


@admin.register(Category)
class CategoryAdmin(SortableModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)
    sortable = 'id'


@admin.register(Testimonial)
class TestimonialAdmin(SortableModelAdmin):
    search_fields = ('title',)
    list_display = ('title',)
    sortable = 'id'


@admin.register(Blog)
class BlogAdmin(SortableModelAdmin):
    search_fields = ('title',)
    list_display = ('title',)
    sortable = 'id'


@admin.register(Feature)
class FeatureAdmin(SortableModelAdmin):
    search_fields = ('title',)
    list_display = ('title',)
    sortable = 'id'

