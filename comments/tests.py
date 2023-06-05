from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Comment
from photos.models import Photo


class CommentListViewTests(APITestCase):
    """
    Tests the list view for the comments app.
    """
    def setUp(self):
        """
        Sets up a user and photo to be used in the tests.
        """
        self.user1 = User.objects.create_user(
            username='user1', password='password1'
            )
        self.photo1 = Photo.objects.create(
            owner=self.user1,
            title='title 1',
            )

    def test_can_list_comments(self):
        """
        Tests if all comments can be fetched and listed.
        """
        Comment.objects.create(
            owner=self.user1, content='comment 1', photo=self.photo1
            )
        response = self.client.get('/comments/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_comment(self):
        """
        Tests if logged in users can create a comment.
        """
        self.client.force_login(self.user1)
        response = self.client.post('/comments/', {
            'content': 'comment 1',
            'photo': 1,
            })
        self.assertEqual(Comment.objects.all().count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_not_logged_in_user_cannot_create_comment(self):
        """
        Tests if logged out users cannot create a comment.
        """
        response = self.client.post('/comments/', {
            'content': 'comment 1',
            'photo': 1,
            })
        self.assertEqual(Comment.objects.all().count(), 0)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class CommentDetailViewTests(APITestCase):
    """
    Tests the detail view for the comments app.
    """
    def setUp(self):
        """
        Sets up users, photo and comments to be used in the tests.
        """
        self.user1 = User.objects.create_user(
            username='user1', password='password1'
            )
        self.user2 = User.objects.create_user(
            username='user2', password='password2'
            )
        self.photo1 = Photo.objects.create(
            owner=self.user1,
            title='title 1',
            )
        Comment.objects.create(
            owner=self.user1, photo=self.photo1
            )
        Comment.objects.create(
            owner=self.user2, photo=self.photo1
            )

    def test_can_retrieve_comment_by_valid_id(self):
        """
        Tests if a commment with a valid id can be fetched and viewed.
        """
        response = self.client.get('/comments/1/')
        self.assertEqual(response.data['photo'], 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_retrieve_comment_by_invalid_id(self):
        """
        Tests if it is possible to fetch and view a
        comment with an invalid id.
        """
        response = self.client.get('/comments/4007/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_comment(self):
        """
        Tests if a user can update their own comment.
        """
        self.client.force_login(self.user1)
        response = self.client.put(
            '/comments/1/', {'content': 'edited comment'}
            )
        comment = Comment.objects.filter(pk=1).first()
        self.assertEqual(comment.content, 'edited comment')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_update_another_users_comment(self):
        """
        Tests if a user cannot edit another user's comment.
        """
        self.client.force_login(self.user1)
        response = self.client.put(
            '/comments/2/', {'content': 'edited comment'}
            )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_delete_own_photo_comment(self):
        """
        Tests if a user can delete their own comment.
        """
        self.client.force_login(self.user1)
        response = self.client.delete('/comments/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Comment.objects.all().count(), 1)

    def test_user_cannot_delete_another_users_comment(self):
        """
        Tests if a user can delete another user's comment.
        """
        self.client.force_login(self.user1)
        response = self.client.delete('/comments/2/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Comment.objects.all().count(), 2)


class CommentModelTests(APITestCase):
    """
    Tests the comment model.
    """
    def test_model_returns_comment_content(self):
        """
        Tests if the comment content is returned from the model.
        """
        user = User.objects.create_user(
            username='user1', password='password1'
            )
        photo = Photo.objects.create(
            owner=user,
            title='title 1',
            )
        Comment.objects.create(
            owner=user, photo=photo, content='comment content'
            )
        self.assertEquals(str(Comment.objects.first()), "comment content")
