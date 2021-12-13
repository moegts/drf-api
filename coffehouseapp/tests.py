from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import CoffeHouse

# Create your tests here.


class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(
            username='testuser', password='password')
        test_user.save()

        test_post = CoffeHouse.objects.create(
            cheff=test_user,
            drink='coffee',
            description='Hot drink with amazing kinds'
        )
        test_post.save()

    def test_blog_content(self):
        post = CoffeHouse.objects.get(id=1)
        actual_cheff = str(post.cheff)
        actual_drink = str(post.drink)
        actual_description = str(post.description)
        self.assertEqual(actual_cheff, 'testuser')
        self.assertEqual(actual_drink, 'coffee')
        self.assertEqual(
            actual_description, 'Hot drink with amazing kinds')