import uuid
from datetime import timedelta

from django.conf import settings
from django.contrib.auth.hashers import make_password, check_password
from django.core.cache import cache
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
    accessed = models.IntegerField(default=0)

    def update_accessed(self):
        self.accessed += 1
        self.save()

    @classmethod
    def get_stats(cls):
        return cls._transform(cls._query_stats())

    @classmethod
    def _query_stats(cls):
        return cls.objects.filter(accessed__gt=0) \
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


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, primary_key=True, related_name='profile', on_delete=models.CASCADE
    )
    user_agent = models.CharField(max_length=1024, blank=True)

    @classmethod
    def get_user_agent_cache_key(cls, request):
        return 'user_agent_{}'.format(request.user.pk)

    @classmethod
    def get_last_user_agent_cached(cls, request):
        cache_key = cls.get_user_agent_cache_key(request)
        user_agent = cache.get(cache_key)
        if user_agent is None:
            user_agent = request.user.profile.user_agent
            cache.set(cache_key, user_agent)
        return user_agent

    @classmethod
    def get_last_user_agent_and_update_if_changed_cached(cls, request):
        last_user_agent = cls.get_last_user_agent_cached(request)
        current_user_agent = request.META.get('HTTP_USER_AGENT')
        if last_user_agent != current_user_agent:
            cache_key = cls.get_user_agent_cache_key(request)
            request.user.profile.user_agent = current_user_agent
            request.user.profile.save()
            cache.set(cache_key, current_user_agent)
        return last_user_agent

