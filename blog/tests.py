from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post, Comment

User = get_user_model()


class UserTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user(
            username='freddy123', password='abc123')

    def test_user_pwd(self):
        checked = self.user_a.check_password('abc123')
        self.assertTrue(checked)


class PostTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user(
            username='freddy', password='abc123')
        self.post_a = Post.objects.create(
            title='hello-world', content='good morning', author=self.user_a)
        self.post_b = Post.objects.create(
            title='hello-earth', content='good night', author=self.user_a)
        self.comment_a = Comment.objects.create(
            post=self.post_a, user=self.user_a, comment_text='nice post')
        self.comment_a = Comment.objects.create(
            post=self.post_b, user=self.user_a, comment_text='nice post')

    def test_post(self):
        self.assertEquals(self.post_a.title, 'hello-world')

    def test_user_post_reverse_counts(self):
        user = self.user_a
        qs = user.post_set.all()
        self.assertEquals(qs.count(), 2)

    def test_user_post_counts(self):
        user = self.user_a
        qs = Post.objects.filter(author=user)
        self.assertEquals(qs.count(), 2)


    def test_post_comment_reverse_counts(self):
        qs = self.post_a.comment_set.all()
        self.assertEquals(qs.count(), 1)


    def test_post_comment_reverse_counts(self):
        qs = Comment.objects.filter(post = self.post_a)
        self.assertEquals(qs.count(), 1)


    def test_comment_user_reverse(self):
        user = self.user_a
        qs = Comment.objects.filter(post__author = user)
        print(qs)
        self.assertEqual(qs.count(),2)