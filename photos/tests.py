from django.contrib.auth.models import User
from .models import Photo
from rest_framework import status
from rest_framework.test import APITestCase


class PhotoListViewTests(APITestCase):
    """
    Tests the list view for the photos app.
    """
    def setUp(self):
        """
        Sets up a user to be used in the tests.
        """
        self.user1 = User.objects.create_user(
            username='user1', password='password1'
            )

    def test_can_list_photos(self):
        """
        Tests all photos can be fetched and listed.
        """
        Photo.objects.create(
            owner=self.user1, title='test title'
            )
        response = self.client.get('/photos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_photo_post(self):
        """
        Tests if a logged in user can create a photo post.
        """
        self.client.force_login(self.user1)
        response = self.client.post('/photos/', {
            'title': 'test title',
            })
        self.assertEqual(Photo.objects.all().count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cannot_create_photo_post(self):
        """
        Tests if a logged out user cannot create a photo post.
        """
        response = self.client.post('/photos/', {
            'title': 'test title',
            })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PhotoDetailViewTests(APITestCase):
    """
    Tests the detail view for the photos app.
    """
    def setUp(self):
        """
        Sets up users and photos to be used in the tests.
        """
        self.user1 = User.objects.create_user(
            username='user1', password='password1'
            )
        self.user2 = User.objects.create_user(
            username='user2', password='password2'
            )
        Photo.objects.create(
            owner=self.user1, title='title 1', description='user1 content'
        )
        Photo.objects.create(
            owner=self.user2, title='title 2', description='user2 content'
        )

    def test_can_retrieve_photo_by_valid_id(self):
        """
        Tests if a photo with a valid id can be fetched and viewed.
        """
        response = self.client.get('/photos/1/')
        self.assertEqual(response.data['title'], 'title 1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_retrieve_photo_by_invalid_id(self):
        """
        Tests if it is possible to fetch and view a photo with an invalid id.
        """
        response = self.client.get('/photos/4007/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_photo_post(self):
        """
        Tests if a user can update their own photo post.
        """
        self.client.force_login(self.user1)
        response = self.client.put('/photos/1/', {'title': 'edited title'})
        photo = Photo.objects.filter(pk=1).first()
        self.assertEqual(photo.title, 'edited title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_update_another_user_photo_post(self):
        """
        Tests if a user cannot edit another user's photo post.
        """
        self.client.force_login(self.user1)
        response = self.client.put('/photos/2/', {'title': 'edited title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_delete_own_photo_post(self):
        """
        Tests if a user can delete their own photo post.
        """
        self.client.force_login(self.user1)
        response = self.client.delete('/photos/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Photo.objects.all().count(), 1)

    def test_user_cannot_delete_another_users_photo_post(self):
        """
        Tests if a user cannot delete another user's photo post.
        """
        self.client.force_login(self.user1)
        response = self.client.delete('/photos/2/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Photo.objects.all().count(), 2)


class PhotoModelTests(APITestCase):
    """
    Tests the photo model.
    """
    def test_model_returns_id_and_title_string(self):
        """
        Tests if the correct string with the photo id and title
        is returned from the model.
        """
        user1 = User.objects.create_user(
            username='user1', password='password1'
            )
        Photo.objects.create(
            owner=user1, title='title 1'
        )
        self.assertEquals(str(Photo.objects.first()), "1 title 1")
