from django.contrib.auth import get_user_model
from django.test import TestCase


class TestCustomPasswordChangeView(TestCase):
    
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', email='test@gmail.com', password='pass')
        
    
    def test_get_success(self):
        logged_in = self.client.login(username='test', email=self.user.email, password='pass')
        self.assertTrue(logged_in)
        
        response = self.client.get('/accounts/password/change/')
        self.assertTemplateUsed(response, 'account/password_change.html')