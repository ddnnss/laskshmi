from django.db import models
from django.db.models.signals import post_save, post_delete
from customuser.models import User, Guest
from item.models import Item, PromoCode


class OrderStatus(models.Model):
    name = models.CharField('Статус для заказа', max_length=100, blank=False)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = "Статус для заказа"
        verbose_name_plural = "Статусы для заказов"

class Order(models.Model):
    client = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.SET_NULL,
                               verbose_name='Заказ клиента')
    guest = models.ForeignKey(Guest, blank=True, null=True, default=None, on_delete=models.SET_NULL,
                              verbose_name='Заказ гостя')
    promo_code = models.ForeignKey(PromoCode, blank=True, null=True, default=None, on_delete=models.SET_NULL,
                              verbose_name='Использованный промо-код')
    status = models.ForeignKey(OrderStatus, blank=True, null=True, default=None, on_delete=models.SET_NULL,
                              verbose_name='Статус заказа')
    total_price = models.IntegerField('Общая стоимость заказа', default=0)
    is_complete = models.BooleanField('Заказ выполнен ?', default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return 'Заказ № %s . Статус: %s ' % (self.id, self.is_complete)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class ItemsInOrder(models.Model):
    order = models.ForeignKey(Order, blank=False, null=True, default=None, on_delete=models.SET_NULL,
                              verbose_name='В заказе')
    item = models.ForeignKey(Item, blank=False, null=True, default=None, on_delete=models.SET_NULL,
                              verbose_name='Товар')
    number = models.IntegerField('Кол-во', blank=True, null=True, default=0)
    current_price = models.IntegerField('Цена за ед.', default=0)
    total_price = models.IntegerField('Общая стоимость', default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.item.discount > 0:
            self.current_price = self.item.price - (self.item.price * self.item.discount / 100)
        else:
            self.current_price = self.item.price
        self.total_price = self.number * self.current_price

        super(ItemsInOrder, self).save(*args, **kwargs)


    def __str__(self):
        return 'Товар : %s . В заказе № %s .' % (self.item.name, self.order.id)

    class Meta:
        verbose_name = "Товар в заказе"
        verbose_name_plural = "Товары в заказах"


def ItemsInOrder_post_save(sender,instance,**kwargs):
    order = instance.order
    order_total_price = 0
    all_items_in_order = ItemsInOrder.objects.filter(order=order)
    for item in all_items_in_order:
        order_total_price += item.total_price
    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)


post_delete.connect(ItemsInOrder_post_save, sender=ItemsInOrder)
post_save.connect(ItemsInOrder_post_save, sender=ItemsInOrder)