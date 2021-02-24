from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone

from ..models import Post


class TestPostListView(TestCase):
    
    def setUp(self):
        self.user1 = get_user_model().objects.create_user(username='test_user1', email='test_user1@gmail.com', password='pass1')
        self.user2 = get_user_model().objects.create_user(username='test_user2', email='test_user2@gmail.com', password='pass2')
        self.post1 = Post.objects.create(writer=self.user1, title='title1', text='text1', published_date=timezone.now(), is_private=False)
        self.post2 = Post.objects.create(writer=self.user1, title='title2', text='text2', published_date=timezone.now(), is_private=True)
        self.post3 = Post.objects.create(writer=self.user2, title='title3', text='text3', published_date=timezone.now(), is_private=False)
        self.post4 = Post.objects.create(writer=self.user2, title='title4', text='text4', published_date=timezone.now(), is_private=True)
    
    
    def test_get(self):
        """
        User can see public posts.
        """
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'blog/post_list.html')
        
        posts = list(response.context['posts'])
        self.assertIn(self.post1, posts)
        self.assertIn(self.post3, posts)
        
    
class TestPostListPrivateView(TestCase):
    
    def setUp(self):
        self.user1 = get_user_model().objects.create_user(username='test_user1', email='test_user1@gmail.com', password='pass1')
        self.user2 = get_user_model().objects.create_user(username='test_user2', email='test_user2@gmail.com', password='pass2')
        self.post1 = Post.objects.create(writer=self.user1, title='title1', text='text1', published_date=timezone.now(), is_private=False)
        self.post2 = Post.objects.create(writer=self.user1, title='title2', text='text2', published_date=timezone.now(), is_private=True)
        self.post3 = Post.objects.create(writer=self.user2, title='title3', text='text3', published_date=timezone.now(), is_private=False)
        self.post4 = Post.objects.create(writer=self.user2, title='title4', text='text4', published_date=timezone.now(), is_private=True)
        
    def test_get_without_login(self):
        """
        Without login, user will redirect to account_login
        """
        response = self.client.get('/private/')
        self.assertRedirects(response, '/accounts/login/')

    def test_get_with_login(self):
        """
        With login, user can see user owned posts
        """
        logged_in = self.client.login(username='test_user1', email='test_user1@gmail.com', password='pass1')
        self.assertTrue(logged_in)
        response = self.client.get('/private/')
        self.assertTemplateUsed(response, 'blog/post_list.html')
        
        posts = list(response.context['posts'])
        self.assertIn(self.post1, posts)
        self.assertIn(self.post2, posts)