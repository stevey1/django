from django.test import TestCase
from cookbook.ingredients.models import Category


class test_models(TestCase):
    fixtures = ['ingredients.json', ]

    def test_get_category(self):
        c = Category.objects.get(pk=1)
        self.assertEqual(c.id, 1)
