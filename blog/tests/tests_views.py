from django.test import TestCase,Client

from ..views.views import adderTest

class TestAdderTestView(TestCase):

    def setUp(self):
        self.client = Client()

    def get(self):


