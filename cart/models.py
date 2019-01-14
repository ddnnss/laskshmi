from django.db import models
from customuser.models import User, Guest
from item.models import Item

class Cart(models.Model):
    client = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.SET_NULL,
                               verbose_name='Корзина клиента')
    guest = models.ForeignKey(Guest, blank=True, null=True, default=None, on_delete=models.SET_NULL,
                              verbose_name='Корзина гостя')
    item = models.ForeignKey(Item, blank=True, null=True, default=None, on_delete=models.SET_NULL,
                              verbose_name='Товар')
    number = models.IntegerField('Кол-во', blank=True, null=True, default=0)
    current_price = models.IntegerField('Цена за ед.', default=0)
    total_price = models.IntegerField('Общая стоимость', default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Корзина № %s ' % self.id

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

    def save(self, *args, **kwargs):
        if self.item.discount > 0:
            self.current_price = self.item.price - (self.item.price * self.item.discount / 100)
        else:
            self.current_price = self.item.price
        self.total_price = self.number * self.current_price

        super(Baskets, self).save(*args, **kwargs)
