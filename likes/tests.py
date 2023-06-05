from django.contrib.auth.models import User
from .models import Like
from photos.models import Photo
from rest_framework import status
from rest_framework.test import APITestCase


class LikeListViewTests(APITestCase):
    """
    Tests the list view for the likes app.
    """
    def setUp(self):
        """
        Sets up user and photo to be used in the tests.
        """
        self.user1 = User.objects.create_user(
            username='user1', password='password1'
            )
        self.photo1 = Photo.objects.create(
            owner=self.user1, title='test title'
            )

    def test_can_list_likes(self):
        """
        Tests all likes can be fetched and listed.
        """
        Like.objects.create(
            owner=self.user1, photo=self.photo1
            )
        response = self.client.get('/likes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_like_photo(self):
        """
        Tests if logged in users can like a photo.
        """
        self.client.force_login(self.user1)
        response = self.client.post('/likes/', {
            'photo': 1,
            })
        self.assertEqual(Like.objects.all().count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_not_logged_in_user_cannot_like_photo(self):
        """
        Tests if logged out users cannot like a photo.
        """
        response = self.client.post('/likes/', {
            'photo': 1,
            })
        self.assertEqual(Like.objects.all().count(), 0)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class LikeDetailViewTests(APITestCase):
    """
    Tests the detail view for the likes app.
    """
    def setUp(self):
        """
        Sets up users, photos, and likes to be used in the tests.
        """
        self.user1 = User.objects.create_user(
            username='user1', password='password1'
            )
        self.user2 = User.objects.create_user(
            username='user2', password='password2'
            )
        self.photo1 = Photo.objects.create(
            owner=self.user1, title='test title 1'
            )
        self.photo2 = Photo.objects.create(
            owner=self.user1, title='test title 2'
            )
        Like.objects.create(
            owner=self.user1, photo=self.photo1
            )
        Like.objects.create(
            owner=self.user2, photo=self.photo2
            )

    def test_can_retrieve_like_by_valid_id(self):
        """
        Tests if a like with a valid id can be fetched and viewed.
        """
        response = self.client.get('/likes/1/')
        self.assertEqual(response.data['photo'], 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_retrieve_like_by_invalid_id(self):
        """
        Tests if it is possible to fetch and view a like with an invalid id.
        """
        response = self.client.get('/likes/4007/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_remove_own_like(self):
        """
        Tests if a user can remove their own like on a photo.
        """
        self.client.force_login(self.user1)
        response = self.client.delete('/likes/1/')
        self.assertEqual(Like.objects.all().count(), 1)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cannot_remove_another_users_like(self):
        """
        Test if a user can remove another user's like on a photo.
        """
        self.client.force_login(self.user1)
        response = self.client.delete('/likes/2/')
        self.assertEqual(Like.objects.all().count(), 2)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class LikeModelTests(APITestCase):
    """
    Tests the like model
    """
    def test_model_returns_owner_and_photo_string(self):
        """
        Tests if the correct string with the like owner and photo
        is returned from the model.
        """
        user = User.objects.create_user(
            username='user', password='password1'
            )
        photo = Photo.objects.create(
            owner=user, title='test title'
            )
        Like.objects.create(
            owner=user, photo=photo
            )
        self.assertEquals(str(Like.objects.first()), "user 1 test title")
