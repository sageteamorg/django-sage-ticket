from django.db.models import QuerySet


class TicktingQueryAccess(QuerySet):
    def get_actives(self):
        return self.filter(is_unread=True)

    def get_archive(self):
        return self.filter(is_unread=True)
