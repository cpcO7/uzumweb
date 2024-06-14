import uuid

from django.db.models import Model, DateTimeField, CharField, SlugField, UUIDField
from django.utils.text import slugify


class TimeBaseModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SlugBaseModel(Model):
    slug = SlugField(max_length=255, unique=True, editable=False)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = self.generate_slug()
        super().save(force_insert, force_update, using, update_fields)

    def generate_slug(self):
        slug = slugify(self.get_slug_source())
        num = 1

        while self.__class__.objects.filter(slug=slug).exists():
            slug += f"-{num}"
            num += 1
        return slug

    def get_slug_source(self):
        raise NotImplementedError("Subclasses must implement get_slug_source method")

    class Meta:
        abstract = True


class UuidBaseModel(Model):
    # id = UUIDField(db_default=RandomUUID, primary_key=True, editable=False) # for Postgres
    id = UUIDField(default=uuid.uuid4, primary_key=True, editable=False)  # basic for sqlite

    class Meta:
        abstract = True


class BaseModel(TimeBaseModel, SlugBaseModel):
    title = CharField(max_length=255)

    def get_slug_source(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        abstract = True
