from django.db.models import IntegerField, TextField, ImageField, CharField, FileField, ForeignKey, CASCADE, \
    BooleanField, PositiveIntegerField, JSONField, Model
from django_ckeditor_5.fields import CKEditor5Field

from core.models.base import SlugBaseModel, BaseModel, TimeBaseModel


class Category(SlugBaseModel):
    title = CharField(max_length=255)
    icon = FileField(upload_to='category/icons', null=True, blank=True)
    parent = ForeignKey('self', CASCADE, null=True, blank=True)

    def get_slug_source(self):
        return self.title


class Shop(BaseModel):
    description = TextField()
    banner = ImageField(upload_to='shop/banner')
    avatar = ImageField(upload_to='shop/avatar')
    logo = ImageField(upload_to='shop/logo/')


class Product(BaseModel):
    price = IntegerField()
    quantity = PositiveIntegerField(default=0, db_default=0)
    seller = ForeignKey('core.Shop', CASCADE, related_name='products')
    category = ForeignKey('core.Category', CASCADE, related_name='products')
    description = CKEditor5Field(null=True, blank=True)
    attributes = JSONField(default=dict, null=True, blank=True)
    reviews_count = PositiveIntegerField(default=0, db_default=0)


class Comment(Model):
    comment_type: CharField(max_length=25)
    comment = CKEditor5Field()
    product = ForeignKey('core.Product', CASCADE, related_name='comments')


class ProductImage(TimeBaseModel):
    image = ImageField(upload_to='product/images/%Y/%m/%d')
    color = CharField(max_length=25, blank=True, null=True)
    product = ForeignKey('core.Product', CASCADE)


class Review(TimeBaseModel):
    text = TextField()
    product = ForeignKey('core.Product', CASCADE, related_name='reviews')
    user = ForeignKey('core.User', CASCADE, related_name='reviews')
    reply = ForeignKey('self', CASCADE, null=True, blank=True, related_name='reviews')


class ReviewImage(TimeBaseModel):
    image = ImageField(upload_to='Review/images/%Y/%m/%d')
    comment = ForeignKey('core.Review', CASCADE)
    author = ForeignKey('core.User', CASCADE)
    is_anonymous = BooleanField(default=False)


class Badge(BaseModel):
    text_color = CharField(max_length=15)
    background_color = CharField(max_length=15)
    description = CKEditor5Field(null=True, blank=True)
