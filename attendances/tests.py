from django.contrib.auth.models import User
from .models import Attendance
from tours.models import Tour
from rest_framework import status
from rest_framework.test import APITestCase


class AttendanceListViewTests(APITestCase):
    """
    Tests the list view for the attendance app.
    """
    def setUp(self):
        """
        Sets up a user and tour to be used in the tests.
        """
        self.user1 = User.objects.create_user(
            username='user1', password='password1'
            )
        self.tour1 = Tour.objects.create(
            title='title 1',
            owner=self.user1,
            start_date='2024-11-11',
            end_date='2024-12-12',
            booking_means='book online',
            country='England',
            city='London'
            )

    def test_can_list_attendances(self):
        """
        Tests if all attendances can be fetched and listed.
        """
        Attendance.objects.create(
            owner=self.user1, tour=self.tour1
            )
        response = self.client.get('/attendances/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_mark_attendance(self):
        """
        Tests if logged in users can mark tour attendance.
        """
        self.client.force_login(self.user1)
        response = self.client.post('/attendances/', {
            'tour': 1,
            })
        self.assertEqual(Attendance.objects.all().count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_not_logged_in_user_cannot_mark_attendance(self):
        """
        Tests if logged out users cannot mark tour attendance.
        """
        response = self.client.post('/attendances/', {
            'tour': 1,
            })
        self.assertEqual(Attendance.objects.all().count(), 0)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class AttendanceDetailViewTests(APITestCase):
    """
    Tests the detail view for the attendance app.
    """
    def setUp(self):
        """
        Sets up users, tours and attendances to be used in the tests.
        """
        self.user1 = User.objects.create_user(
            username='user1', password='password1'
            )
        self.user2 = User.objects.create_user(
            username='user2', password='password2'
            )
        self.tour = Tour.objects.create(
            title='title 1',
            owner=self.user1,
            start_date='2024-11-11',
            end_date='2024-12-12',
            booking_means='book online',
            country='England',
            city='London'
            )
        Attendance.objects.create(
            owner=self.user1, tour=self.tour
            )
        Attendance.objects.create(
            owner=self.user2, tour=self.tour
            )

    def test_can_retrieve_attendance_by_valid_id(self):
        """
        Tests if an attendance with a valid id can be fetched and viewed.
        """
        response = self.client.get('/attendances/1/')
        self.assertEqual(response.data['tour'], 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_retrieve_attendance_by_invalid_id(self):
        """
        Tests if it is possible to fetch and view an
        attendance with an invalid id.
        """
        response = self.client.get('/attendances/4007/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_unmark_own_attendance(self):
        """
        Tests if a user can unmark their own attendance on a tour.
        """
        self.client.force_login(self.user1)
        response = self.client.delete('/attendances/1/')
        self.assertEqual(Attendance.objects.all().count(), 1)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cannot_unmark_another_users_attendance(self):
        """
        Tests if a user cannot unmark another user's attendance on a tour.
        """
        self.client.force_login(self.user1)
        response = self.client.delete('/attendances/2/')
        self.assertEqual(Attendance.objects.all().count(), 2)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class AttendanceModelTests(APITestCase):
    """
    Tests the attendance model
    """
    def test_model_returns_owner_and_tour_string(self):
        """
        Tests if the correct string with the attendance owner and tour
        is returned from the model.
        """
        user = User.objects.create_user(
            username='user', password='password1'
            )
        tour = Tour.objects.create(
            title='title 1',
            owner=user,
            start_date='2024-11-11',
            end_date='2024-12-12',
            booking_means='book online',
            country='England',
            city='London'
            )
        Attendance.objects.create(
            owner=user, tour=tour
            )
        self.assertEquals(str(Attendance.objects.first()), "user 1 title 1")
