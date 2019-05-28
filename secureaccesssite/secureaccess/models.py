import uuid
from datetime import timedelta

from django.contrib.auth.hashers import make_password, check_password
from django.db import models
from django.db.models import Count, Q
from django.utils import timezone
from django.utils.crypto import get_random_string

from secureaccess.utils import format_date


class AbstractSecureAccess(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    shareable_link = models.UUIDField(default=uuid.uuid4, unique=True)
    password = models.CharField(max_length=128)

    class Meta:
        abstract = True

    @classmethod
    def get_valid_obj(cls, shareable_link):
        return cls.objects.filter(
            shareable_link=shareable_link,
            created_at__gt=timezone.now() - timedelta(hours=24)
        ).first()

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def make_random_password(self):
        raw_password = get_random_string()
        self.set_password(raw_password)
        return raw_password

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)


class Element(AbstractSecureAccess):
    file = models.FileField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    accessed = models.BooleanField(default=False)

    def update_accessed(self):
        if not self.accessed:
            self.accessed = True
            self.save()

    @classmethod
    def get_stats(cls):
        return cls._transform(cls._query_stats())

    @classmethod
    def _query_stats(cls):
        return cls.objects.filter(accessed=True) \
            .values('created_at__date') \
            .annotate(
                files=Count('file', ~(Q(file=None) | Q(file=''))),
                links=Count('url', Q(url__isnull=False))
            )

    @classmethod
    def _transform(cls, query):
        """
        Transform list of
            {'created_at__date': datetime.date(2019, 1, 4), 'files': 2, 'links': 0}

        into dict with
            "2019-01-04": {
                "files": 2,
                "links": 0
            },
        """
        result = {}
        for o in query:
            str_date = format_date(o.pop('created_at__date'))
            result[str_date] = o
        return result

