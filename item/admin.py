from django.contrib import admin
from .models import *



class ImagesInline (admin.TabularInline):
    model = ItemImage
    extra = 0

class ItemsInline (admin.TabularInline):
    model = Item
    extra = 0

class ItemsInlineCollections (admin.TabularInline):
    model = Item.collection.through
    extra = 0

class FilterInline(admin.TabularInline):
    model = Filter
    extra = 0

class ItemAdmin(admin.ModelAdmin):
    # list_display = ['name','discount']
    #list_display = [field.name for field in Item._meta.fields]
    inlines = [ImagesInline]
    search_fields = ('name', 'name_slug','article')
    # exclude = ['info'] #не отображать на сранице редактирования
    class Meta:
        model = Item

class SubcatAdmin(admin.ModelAdmin):
    # list_display = ['name','discount']
    list_display = [field.name for field in SubCategory._meta.fields]
  #  inlines = [ItemsInline, FilterInline]
    # exclude = ['info'] #не отображать на сранице редактирования
    class Meta:
        model = SubCategory

class CollectionAdmin(admin.ModelAdmin):
    inlines = [ItemsInlineCollections]
    class Meta:
        model = Collection

class FilterAdmin(admin.ModelAdmin):
    search_fields = ('name', 'name_slug')

admin.site.register(Category)
admin.site.register(SubCategory, SubcatAdmin)
admin.site.register(Filter,FilterAdmin)
admin.site.register(Item,ItemAdmin)
admin.site.register(ItemImage)
admin.site.register(Collection,CollectionAdmin)
admin.site.register(PromoCode)