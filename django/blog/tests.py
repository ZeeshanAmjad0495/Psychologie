from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Category
# Create your tests here.


class Test_Create_Post(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='django')
        test_user1 = User.objects.create_user(
            username='testuser1', password='12345678')
        test_post = Post.objects.create(
            category_id=1, title='Test Post', excerpt='Post Excerpt', content='Post Content', author_id=1, status='published')

    def test_blog_content(self):
        post = Post.postobjects.get(id=1)
        cat = Category.objects.get(id=1)
        author = f'{post.author}'
        excerpt = f'{post.excerpt}'
        content = f'{post.content}'
        title = f'{post.title}'
        status = f'{post.status}'
        self.assertEqual(author, 'testuser1')
        self.assertEqual(excerpt, 'Post Excerpt')
        self.assertEqual(content, 'Post Content')
        self.assertEqual(title, 'Test Post')
        self.assertEqual(status, 'published')
        self.assertEqual(str(post), 'Test Post')
        self.assertEqual(str(cat), 'django')
