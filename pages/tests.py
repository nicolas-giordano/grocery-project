from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView
# Create your tests here.


class HomePageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('home')
        self.resp = self.client.get(url)

    def test_homepage_status(self):
        self.assertEqual(self.resp.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.resp, 'home.html')

    def test_homepage_correct_html(self):
        self.assertContains(self.resp, 'Homepage')

    def test_homepage_wrong_html(self):
        self.assertNotContains(self.resp, 'I am a test case.')

    def test_homepage_url_resolves_view(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)
