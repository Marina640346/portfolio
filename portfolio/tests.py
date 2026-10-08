from django.test import TestCase
from .models import Poll

class PollModelTest(TestCase):
    def test_poll_title(self):
        poll = Poll.objects.create(title="Тестове опитування")
        self.assertEqual(poll.title, "Тестове опитування")
