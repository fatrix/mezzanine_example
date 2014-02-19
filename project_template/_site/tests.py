from django.test import TestCase, Client


class BasicTestCase(TestCase):
    def setUp(self):
    	pass

    def test_main_page_responds_with_ok(self):
    	self.client = Client()
    	response = self.client.get("/")
        self.assertEqual(response.status_code, 200)