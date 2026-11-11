from django.test import TestCase, Client
from django.urls import reverse

class InvitationViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_page_bride(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, 'Pulikkalakath Nikah Invitation')
        self.assertContains(response, 'Mr. Niyas Pulikkalakath')

    def test_ziya_alias(self):
        for path in ['/ziya', '/ziya/']:
            response = self.client.get(path)
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'index.html')

    def test_dinu_page_groom(self):
        for path in ['/dinu', '/dinu/']:
            response = self.client.get(path)
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'dinu.html')
            self.assertContains(response, 'Kollan Thodi Nikah Invitation')
            self.assertContains(response, 'Mr. K.T Kunchi Muhammad')

