# Third Party Stuff
from django.test import TestCase

# nexus Stuff
from nexus.users.models import User
from nexus.social_media.models import Post


class TestPostModel(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(email='f@f.com', password='abc', first_name="F", last_name='B')
        self.super_user = User.objects.create_superuser(email='super@user.com', password='superuser_pass')

    def test_create_post(self):
        post = {
            'posted_at': 'fb'
        }
