from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class TestUrls(TestCase):

    def test_home_page_status_code(self):
        response = self.client.get(reverse("Tasks:add_task"))
        self.assertEqual(response.status_code, 200)

    def test_category_page_uses_correct_template(self):
        response = self.client.get(reverse("Tasks:Category"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "category.html")