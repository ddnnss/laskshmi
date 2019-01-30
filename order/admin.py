from django.contrib import admin
from .models import *

class ItemsInline (admin.TabularInline):
    model = ItemsInOrder
    extra = 0


class OrdersAdmin(admin.ModelAdmin):
    # list_display = ['name','discount']
   # list_display = [field.name for field in Categories._meta.fields]
    list_filter = ('is_complete',)
    inlines = [ItemsInline]
    # exclude = ['info'] #не отображать на сранице редактирования
    class Meta:
        model = Order


admin.site.register(Order, OrdersAdmin)
admin.site.register(OrderStatus)
admin.site.register(OrderShipping)
admin.site.register(OrderPayment)
admin.site.register(ItemsInOrder)
