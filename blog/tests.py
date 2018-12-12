from django.test import TestCase,Client
from .models import Post
from django.contrib.auth import get_user_model
from django.urls import reverse



# Create your tests here.

class BlogTest(TestCase):

    def setUp(self):

        self.user=get_user_model().objects.create_user(
            username='chris',
            email='a@demo.com',
            password='testpassword1234567'
        )
        self.post= Post.objects.create(
            title='A lion',
            author= self.user,
            content='A lion has a tail'
        )

    def test_string_reperesentation(self):
        post= Post(title='A lion')
        self.assertEqual(str(post),post.title)
    
    def test_post_content(self):
        self.assertEqual(f"{self.post.content}",'A lion has a tail')
        self.assertEqual(f"{self.post.title}",'A lion')
        self.assertEqual(f"{self.post.author}",self.user.username)

class TestBlogView(TestCase):

    def setUp(self):
        self.user=get_user_model().objects.create_user(
            username='king',
            password='king1234567',
            email='k@demo.com'
        )

        self.post =Post.objects.create(
            title='Africa',
            content='I love Africa',
            author=self.user
        )

        self.client=Client()


    def test_if_content_exit(self):
        self.assertEqual(f"{self.post.content}",'I love Africa')

    def test_if_home_route_exits(self):
        response=self.client.get('/')
        self.assertEqual(response.status_code,200)

    def test_post_list_view(self):
        response=self.client.get(reverse('home_page'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'home.html')
        self.assertNotContains(response,'This is a chicken')
        self.assertContains(response,'I love Africa')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        non_response=self.client.get('2/post')
        second_non_response=self.client.get('post/20973')
        self.assertEqual(response.status_code,200)
        self.assertEqual(non_response.status_code,404)
        self.assertEqual(second_non_response.status_code,404)
        self.assertTemplateUsed(response,'post_detail.html')



