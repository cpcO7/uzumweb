from django.contrib.postgres.fields import ArrayField
from django.db.models import IntegerField, TextField, ImageField, CharField, FileField, ForeignKey, CASCADE, \
    BooleanField, PositiveIntegerField, JSONField, Model, SlugField, URLField
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field
from mptt.models import MPTTModel, TreeForeignKey

from apps.models.base import BaseModel, TimeBaseModel


class Category(MPTTModel):
    title = CharField(max_length=255)
    slug = SlugField(max_length=255, unique=True, editable=False)
    icon = FileField(upload_to='category/icons', null=True, blank=True)
    adult = BooleanField(db_default=False, blank=True, null=True)
    icon_link = URLField(db_default=False, blank=True, null=True)
    eco = BooleanField(db_default=False, blank=True, null=True)
    seo_meta_tag = CharField(max_length=255, blank=True, null=True)
    seo_header = CharField(max_length=255, blank=True, null=True)
    path = ArrayField(IntegerField(), blank=True, default=list)
    icon_svg = TextField(blank=True, null=True)

    parent = TreeForeignKey('self', CASCADE, null=True, blank=True, related_name='children')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_slug_source(self):
        return self.title

    def __str__(self):
        return self.title


class Shop(BaseModel):
    description = TextField()
    banner = ImageField(upload_to='shop/banner')
    avatar = ImageField(upload_to='shop/avatar')
    owner = ForeignKey('apps.User', CASCADE, related_name='shops')
    logo = ImageField(upload_to='shop/logo/')


class Product(BaseModel):
    price = IntegerField()
    quantity = PositiveIntegerField(default=0, db_default=0)
    video = FileField(upload_to='product/video', null=True, blank=True)
    seller = ForeignKey('apps.Shop', CASCADE, related_name='products')
    category = ForeignKey('apps.Category', CASCADE, related_name='products')
    description = CKEditor5Field(null=True, blank=True)
    attributes = JSONField(default=dict, null=True, blank=True)
    reviews_count = PositiveIntegerField(default=0, db_default=0)


class Comment(Model):
    comment_type: CharField(max_length=25)
    comment = CKEditor5Field()
    product = ForeignKey('apps.Product', CASCADE, related_name='comments')


class ProductImage(TimeBaseModel):
    image = ImageField(upload_to='product/images/%Y/%m/%d')
    color = CharField(max_length=25, blank=True, null=True)
    product = ForeignKey('apps.Product', CASCADE)


class Review(TimeBaseModel):
    text = TextField()
    product = ForeignKey('apps.Product', CASCADE, related_name='reviews')
    user = ForeignKey('apps.User', CASCADE, related_name='reviews')
    reply = ForeignKey('self', CASCADE, null=True, blank=True, related_name='reviews')


class ReviewImage(TimeBaseModel):
    image = ImageField(upload_to='Review/images/%Y/%m/%d')
    comment = ForeignKey('apps.Review', CASCADE)
    author = ForeignKey('apps.User', CASCADE)
    is_anonymous = BooleanField(default=False)


class Badge(BaseModel):
    text_color = CharField(max_length=15)
    background_color = CharField(max_length=15)
    description = CKEditor5Field(null=True, blank=True)


class Region(Model):
    title = CharField(max_length=100)


class District(Model):
    title = CharField(max_length=100)
    region = ForeignKey('apps.Region', CASCADE)


class Wish(TimeBaseModel):
    product = ForeignKey("apps.Product", CASCADE)
    user = ForeignKey("apps.User", CASCADE)

    class Meta:
        unique_together = ('product', 'user')
