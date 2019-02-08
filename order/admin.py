from django.contrib import admin
from .models import *

class ItemsInline (admin.TabularInline):
    model = ItemsInOrder
    readonly_fields = ('image_tag',)
    #list_display = ['id', 'discount']
    extra = 0
    #
    # def get_queryset(self, request):
    #     qs = super(ItemsInline, self).get_queryset(request)
    #     return qs.filter(order_id=self.model.order.id)


class OrdersAdmin(admin.ModelAdmin):
    # list_display = ['name','discount']
   # list_display = [field.name for field in Categories._meta.fields]
    list_filter = ('is_complete',)
    inlines = [ItemsInline]
    readonly_fields = ('order_code', 'promo_code',)
    # exclude = ['info'] #не отображать на сранице редактирования
    class Meta:
        model = Order




admin.site.register(Order, OrdersAdmin)
admin.site.register(OrderStatus)
admin.site.register(OrderShipping)
admin.site.register(OrderPayment)
admin.site.register(ItemsInOrder)
