from django.db.models import Manager

from ..queryset import TicketQueryAccess


class DataAccessLayerManager(Manager):
    def get_queryset(self):
        return TicketQueryAccess(self.model, using=self._db)

    def find_publisher(self, publisher):
        return self.get_queryset().find_publisher(publisher)
