from django.db.models import CharField, BooleanField

from apps.models.base import SlugBaseModel


class DeliveryPoint(SlugBaseModel):
    city = CharField(max_length=100)
    location = CharField(max_length=150)
    fitting_room = BooleanField(db_default=False)
    working_hour = CharField(max_length=150)

    def get_slug_source(self):
        return self.location

    def __str__(self):
        return self.city
