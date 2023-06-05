from django.contrib.auth.models import User
from .models import Profile
from rest_framework import status
from rest_framework.test import APITestCase


class ProfileListViewTests(APITestCase):
    """
    Tests the list view for the profiles app.
    """
    def setUp(self):
        """
        Sets up users to be used in the tests.
        """
        User.objects.create_user(username='user1', password='password1')
        User.objects.create_user(username='user2', password='password2')

    def test_profile_is_created_on_user_creation(self):
        """
        Tests if a profile is automatically created when a user is created.
        """
        self.assertEqual(Profile.objects.all().count(), 2)

    def test_can_list_profiles(self):
        """
        Tests all profiles can be fetched and listed.
        """
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ProfileDetailViewTests(APITestCase):
    """
    Tests the detail view for the profiles app.
    """
    def setUp(self):
        """
        Sets up users to be used in the tests.
        """
        self.user1 = User.objects.create_user(
            username='user1', password='password1'
            )
        self.user2 = User.objects.create_user(
            username='user2', password='password2'
            )

    def test_can_retrieve_profile_by_valid_id(self):
        """
        Tests if a profile with a valid id can be fetched and viewed.
        """
        response = self.client.get('/profiles/1/')
        self.assertEqual(response.data['owner'], 'user1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_retrieve_profile_by_invalid_id(self):
        """
        Tests if it is possible to fetch and view a profile with an invalid id.
        """
        response = self.client.get('/profiles/4007/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_profile(self):
        """
        Tests if a user can update their own profile.
        """
        self.client.force_login(self.user1)
        response = self.client.put(
            '/profiles/1/', {'description': 'a new description'}
            )
        profile = Profile.objects.filter(pk=1).first()
        self.assertEqual(profile.description, 'a new description')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_update_another_users_profile(self):
        """
        Tests if a user cannot edit another user's profile.
        """
        self.client.force_login(self.user1)
        response = self.client.put(
            '/profiles/2/', {'description': 'a new description'}
            )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_delete_own_profile(self):
        """
        Tests if a user can delete their own profile.
        """
        self.client.force_login(self.user1)
        response = self.client.delete('/profiles/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Profile.objects.all().count(), 1)

    def test_user_cannot_delete_another_users_profile(self):
        """
        Tests if a user can delete another user's profile.
        """
        self.client.force_login(self.user1)
        response = self.client.delete('/profiles/2/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Profile.objects.all().count(), 2)


class ProfileModelTests(APITestCase):
    """
    Tests the profile model
    """
    def test_model_returns_profile_owner_string(self):
        """
        Tests if the correct string with the profile
        owner is returned from the model.
        """
        User.objects.create_user(
            username='user3', password='password3'
            )
        self.assertEquals(str(Profile.objects.first()), "user3's profile")
