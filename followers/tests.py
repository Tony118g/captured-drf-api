from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Follower


class FollowerListViewTests(APITestCase):
    """
    Tests the list view for the followers app.
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

    def test_can_list_followers(self):
        """
        Tests if all followers can be fetched and listed.
        """
        Follower.objects.create(
            owner=self.user1, followed=self.user2
            )
        response = self.client.get('/followers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_follow_a_user(self):
        """
        Tests if logged in users can follow other users.
        """
        self.client.force_login(self.user1)
        response = self.client.post('/followers/', {
            'followed': 2,
            })
        self.assertEqual(Follower.objects.all().count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_not_logged_in_user_cannot_follow_a_user(self):
        """
        Tests if logged out users cannot follow another user.
        """
        response = self.client.post('/followers/', {
            'followed': 2,
            })
        self.assertEqual(Follower.objects.all().count(), 0)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class FollowerDetailViewTests(APITestCase):
    """
    Tests the detail view for the followers app.
    """
    def setUp(self):
        """
        Sets up users and followers to be used in the tests.
        """
        self.user1 = User.objects.create_user(
            username='user1', password='password1'
            )
        self.user2 = User.objects.create_user(
            username='user2', password='password2'
            )
        self.user3 = User.objects.create_user(
            username='user3', password='password3'
            )

        Follower.objects.create(owner=self.user1, followed=self.user2)
        Follower.objects.create(owner=self.user2, followed=self.user3)

    def test_can_retrieve_follower_by_valid_id(self):
        """
        Tests if a follower with a valid id can be fetched and viewed.
        """
        response = self.client.get('/followers/1/')
        self.assertEqual(response.data['followed'], 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_retrieve_follower_by_invalid_id(self):
        """
        Tests if it is possible to fetch and view a
        follower with an invalid id.
        """
        response = self.client.get('/followers/4007/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_unfollow_a_user(self):
        """
        Tests if a user can unfollow another user.
        """
        self.client.force_login(self.user1)
        response = self.client.delete('/followers/1/')
        self.assertEqual(Follower.objects.all().count(), 1)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cannot_unfollow_on_another_users_behalf(self):
        """
        Tests if a user cannot unfollow users on another user's behalf.
        """
        self.client.force_login(self.user1)
        response = self.client.delete('/followers/2/')
        self.assertEqual(Follower.objects.all().count(), 2)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class FollowerModelTests(APITestCase):
    """
    Tests the follower model
    """
    def test_model_returns_owner_and_followed_string(self):
        """
        Tests if the correct string with the follower owner and followed field
        is returned from the model.
        """
        user1 = User.objects.create_user(
            username='user1', password='password1'
            )
        user2 = User.objects.create_user(
            username='user2', password='password2'
            )

        Follower.objects.create(
            owner=user1, followed=user2
            )
        self.assertEquals(str(Follower.objects.first()), "user1 user2")
