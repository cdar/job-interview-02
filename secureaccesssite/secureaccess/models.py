import uuid
from datetime import timedelta

from django.contrib.auth.hashers import make_password, check_password
from django.db import models
from django.utils import timezone
from django.utils.crypto import get_random_string


class AbstractSecureAccess(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    shareable_link = models.UUIDField(default=uuid.uuid4, unique=True)
    password = models.CharField(max_length=128, )

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
