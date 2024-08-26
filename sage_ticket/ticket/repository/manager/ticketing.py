from django.db.models import Manager

from ..queryset import TicktingQueryAccess


class DataAccessLayerManager(Manager):
    def get_queryset(self):
        return TicktingQueryAccess(self.model, using=self._db)

    def find_publisher(self, publisher):
        return self.get_queryset().find_publisher(publisher)
