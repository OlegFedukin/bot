from django.test import TestCase
from .models import Games

class GamesTestCase(TestCase):
    def test_model_name(self):
        game1 = Games.objects.create(name="tigr", price=34)
        self.assertEqual(game1.name, "tigr")

    def test_model_price(self):
        game1 = Games.objects.create(name="tigr", price=676)
        self.assertEqual(game1.price, 676)
