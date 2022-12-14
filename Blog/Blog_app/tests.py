from django.test import TestCase
from django.urls import reverse
from Blog_app.models import Account, Post


# Create your tests here.

class AccountTest(TestCase):
    pass


class PostTest(TestCase):

    def setUp(self):
        Post.objects.create(text='just a test')

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEquals(expected_object_name, 'just a test')

    def test_post_list_view(self):
        response = self.client.get(reverse('posts'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'just a test')
        self.assertTemplateUsed(response, '.html')  # page posts

    pass


if __name__ == '__main__':
    TestCase()
