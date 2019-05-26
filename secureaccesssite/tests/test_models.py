from datetime import timedelta
from functools import partial
from unittest import TestCase
from unittest.mock import patch

from django.test import TestCase as DjangoTestCase
from django.utils.timezone import now

from tests.models import SecureAccess


class TestAbstractSecureAccessDB(DjangoTestCase):

    @classmethod
    def now_minus_hours(cls, hours):
        return now() - timedelta(hours=hours)

    @classmethod
    @patch('django.utils.timezone.now')
    def setUpClass(cls, mock_now):
        super().setUpClass()

        hours = [36, 25, 24, 12]
        datetimes = [cls.now_minus_hours(i) for i in hours]
        mock_now.side_effect = partial(next, iter(datetimes))

        secure_access_obs = []
        for _ in hours:
            secure_access_obs.append(SecureAccess.objects.create())

        cls.secure_access_obs = secure_access_obs

    def test_get_valid_obj_not_none(self):
        requested_secure_access = self.secure_access_obs[-1]
        secure_access = SecureAccess.get_valid_obj(requested_secure_access.shareable_link)
        self.assertIsNotNone(secure_access)
        self.assertEqual(requested_secure_access.shareable_link, secure_access.shareable_link)

    def test_get_valid_obj_none(self):
        requested_secure_access = self.secure_access_obs[-2]
        secure_access = SecureAccess.get_valid_obj(requested_secure_access.shareable_link)
        self.assertIsNone(secure_access)


class TestAbstractSecureAccessNoDB(TestCase):

    def test_password(self):
        sa = SecureAccess()
        self.assertEqual(sa.password, '')
        sa.set_password('earth')
        self.assertNotIn(sa.password, [None, ''])
        self.assertNotIn('earth', sa.password)
        self.assertTrue(sa.check_password('earth'))

        raw_password = sa.make_random_password()
        self.assertNotIn(sa.password, [None, '', raw_password])
        self.assertTrue(sa.check_password(raw_password))
