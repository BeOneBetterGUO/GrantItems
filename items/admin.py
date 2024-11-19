from django.contrib import admin

from items.models import ItemCategory, Item, ItemStatus


# Register your models here.
class ItemCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'image', 'count', 'type',
                    'status', 'is_consumable', 'overdue', 'link', 'owner', 'create_time']


class ItemStatusAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(ItemCategory, ItemCategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(ItemStatus, ItemStatusAdmin)
