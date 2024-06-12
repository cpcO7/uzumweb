from django.db.models import Model, ForeignKey, CASCADE


class Basket(Model):
    user = ForeignKey('core.User', CASCADE, related_name='basket')
    product = ForeignKey('core.Product', CASCADE, related_name='basket_products')

