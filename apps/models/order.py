from django.db.models import Model, ForeignKey, CASCADE


class Basket(Model):
    user = ForeignKey('apps.User', CASCADE, related_name='basket')
    product = ForeignKey('apps.Product', CASCADE, related_name='basket_products')

