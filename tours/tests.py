from django.contrib.auth.models import User
from .models import Tour
from rest_framework import status
from rest_framework.test import APITestCase


class TourListViewTests(APITestCase):
    """
    Tests the list view for the tours app.
    """
    def setUp(self):
        """
        Sets up users to be used in the tests.
        """
        self.user1 = User.objects.create_user(
            username='user1', password='password1'
            )
        self.staff_user = User.objects.create_user(
            username="staff",
            password="staff_password",
            is_staff=True
        )

    def test_can_list_tours(self):
        """
        Tests all tours can be fetched and listed.
        """
        Tour.objects.create(
            title='title 1',
            owner=self.user1,
            start_date='2024-11-11',
            end_date='2024-12-12',
            booking_means='book online',
            country='England',
            city='London'
            )
        response = self.client.get('/tours/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_staff_user_can_create_tour(self):
        """
        Tests if a logged in staff user can create a tour.
        """
        self.client.force_login(self.staff_user)
        response = self.client.post('/tours/', {
            'title': 'test title',
            'start_date': '2024-11-11',
            'end_date': '2024-12-12',
            'booking_means': 'book online',
            'country': 'England',
            'city': 'London'
            })
        self.assertEqual(Tour.objects.all().count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_non_staff_user_cannot_create_tour(self):
        """
        Tests if a non staff user cannot create a tour.
        """
        self.client.force_login(self.user1)
        response = self.client.post('/tours/', {
            'title': 'test title',
            'start_date': '2024-11-11',
            'end_date': '2024-12-12',
            'booking_means': 'book online',
            'country': 'England',
            'city': 'London'
            })
        self.assertEqual(Tour.objects.all().count(), 0)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class TourDetailViewTests(APITestCase):
    """
    Tests the detail view for the tours app.
    """
    def setUp(self):
        """
        Sets up users and a tour to be used in the tests.
        """
        self.user1 = User.objects.create_user(
            username='user1', password='password1'
            )
        self.staff_user = User.objects.create_user(
            username="staff",
            password="staff_password",
            is_staff=True
        )
        Tour.objects.create(
            title='title 1',
            owner=self.user1,
            start_date='2024-11-11',
            end_date='2024-12-12',
            booking_means='book online',
            country='England',
            city='London'
            )

    def test_can_retrieve_tour_by_valid_id(self):
        """
        Tests if a tour with a valid id can be fetched and viewed.
        """
        response = self.client.get('/tours/1/')
        self.assertEqual(response.data['title'], 'title 1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_retrieve_tour_by_invalid_id(self):
        """
        Tests if it is possible to fetch and view a tour with an invalid id.
        """
        response = self.client.get('/tours/4007/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_staff_user_can_update_tour(self):
        """
        Tests if a staff user can update a tour.
        """
        self.client.force_login(self.staff_user)
        response = self.client.put('/tours/1/', {
            'title': 'edited title',
            'start_date': '2024-11-11',
            'end_date': '2024-12-12',
            'booking_means': 'book online',
            'country': 'England',
            'city': 'London'
            })
        tour = Tour.objects.filter(pk=1).first()
        self.assertEqual(tour.title, 'edited title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_non_staff_user_cannot_update_tour(self):
        """
        Tests if a non staff user cannot edit a tour.
        """
        self.client.force_login(self.user1)
        response = self.client.put('/tours/1/', {'title': 'edited title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_staff_user_can_delete_tour(self):
        """
        Tests if a staff user can delete a tour.
        """
        self.client.force_login(self.staff_user)
        response = self.client.delete('/tours/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Tour.objects.all().count(), 0)

    def test_non_staff_user_cannot_delete_tour(self):
        """
        Tests if a non staff user cannot delete a tour.
        """
        self.client.force_login(self.user1)
        response = self.client.delete('/tours/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Tour.objects.all().count(), 1)


class TourModelTests(APITestCase):
    """
    Tests the tour model.
    """
    def test_model_returns_id_and_title_string(self):
        """
        Tests if the correct string with the tour id and title
        is returned from the model.
        """
        user1 = User.objects.create_user(
            username='user1', password='password1'
            )
        Tour.objects.create(
            title='title 1',
            owner=user1,
            start_date='2024-11-11',
            end_date='2024-12-12',
            booking_means='book online',
            country='England',
            city='London'
            )
        self.assertEquals(str(Tour.objects.first()), "1 title 1")
