from django.contrib import admin
from .models import Category, Dish, Event, Chef, ChefCategory, Gallery, Contact


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_visible', 'sort', 'created_at', 'updated_at')
    list_editable = ('is_visible', 'sort')
    list_filter = ('is_visible', 'created_at', 'updated_at')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'created_at'


class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'ingredients', 'price', 'weight', 'photo', 'is_visible', 'sort', 'created_at', 'updated_at')
    list_editable = ('name', 'ingredients', 'price', 'weight', 'photo', 'is_visible', 'sort')
    list_filter = ('is_visible', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'

@admin.register(Event)
class EventsAdmin(admin.ModelAdmin):
    list_display = ('title', 'sort', 'is_visible', 'description', 'photo', 'price', 'created_at', 'updated_at')
    list_editable = ('sort', 'is_visible', 'description', 'photo', 'price')
    list_filter = ('is_visible',)
    date_hierarchy = 'created_at'

@admin.register(ChefCategory)
class ChefCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_visible', 'created_at', 'updated_at')
    list_editable =  ('is_visible', )
    list_filter = ('is_visible', )
    date_hierarchy = 'created_at'

@admin.register(Chef)
class ChefAdmin(admin.ModelAdmin):
    list_display = ('created_at' ,'first_name', 'last_name', 'photo', 'updated_at')
    list_editable = ('first_name', 'last_name', 'photo')
    date_hierarchy = 'created_at'

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'is_visible', 'photo', 'position', 'updated_at')
    list_editable = ('is_visible', 'photo', 'position')
    list_filter = ('is_visible', 'position')
    date_hierarchy ='created_at'

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'address', 'phone', 'email', 'work_days', 'start_time', 'end_time', 'day_off', 'updated_at')
    list_editable = ('address', 'phone', 'email', 'work_days', 'start_time', 'end_time', 'day_off')
    date_hierarchy = 'created_at'