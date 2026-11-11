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

    def test_reception_page_4_to_7(self):
        paths = [
            '/receptoin-4-7',
            '/receptoin-4-7/',
            '/reception-4-7',
            '/reception-4-7/',
            '/reception',
            '/reception/',
        ]
        for path in paths:
            response = self.client.get(path)
            self.assertEqual(response.status_code, 200, f"Failed for path {path}")
            self.assertTemplateUsed(response, 'reception.html')
            self.assertContains(response, 'Ziya &amp; Dinu Reception')
            self.assertContains(response, 'RECEPTION CEREMONY')
            self.assertContains(response, '4:00 PM – 7:00 PM')
            self.assertContains(response, '2026-12-04T16:00:00+05:30')
            self.assertContains(response, 'NCC Road, Parappanangadi')

    def test_reception_page_7_to_10(self):
        paths = [
            '/mehandi',
            '/mehandi/',
            '/mehendi',
            '/mehendi/',
            '/reception-7-10',
            '/reception-7-10/',
            '/receptoin-7-10',
            '/receptoin-7-10/',
            '/reception_7_10',
            '/reception_7_10/',
        ]
        for path in paths:
            response = self.client.get(path)
            self.assertEqual(response.status_code, 200, f"Failed for path {path}")
            self.assertTemplateUsed(response, 'reception_7_10.html')
            self.assertContains(response, 'Ziya &amp; Dinu Mehandi')
            self.assertContains(response, 'MEHANDI CEREMONY')
            self.assertContains(response, '7:00 PM – 10:00 PM')
            self.assertContains(response, '2026-12-04T19:00:00+05:30')
            self.assertContains(response, 'NCC Road, Parappanangadi')
