from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import StickyNote


class StickyNotesAppTestCase(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser',
                                             password='testpassword')
        # Create a client instance
        self.client = Client()
        # Log in the user
        self.client.login(username='testuser', password='testpassword')
        # Create a sample sticky note
        self.note = StickyNote.objects.create(
            user=self.user,
            title='Example Note',
            content='This is an example .'
        )

    def test_index_view(self):
        # Test the index view
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_notes_hub_view(self):
        # Test the notes hub view
        response = self.client.get(reverse('notes_hub'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes_hub.html')
        self.assertContains(response, 'Example Note')

    def test_add_note_view(self):
        # Test adding a new note
        url = reverse('add_note')
        response = self.client.post(url, {
            'title': 'New Note',
            'content': 'This is a new note.'
        })
        # Check page is redirected
        self.assertEqual(response.status_code, 302)

        # Verify the note was added
        new_note = StickyNote.objects.get(title='New Note')
        self.assertEqual(new_note.content, 'This is a new note.')
        self.assertEqual(new_note.user, self.user)

    def test_edit_note_view(self):
        # Test editing an existing note
        url = reverse('edit_note', args=[self.note.id])
        response = self.client.post(url, {
            'title': 'Updated Note',
            'content': 'This is an updated note.'
        })
        # Check page is redirected
        self.assertEqual(response.status_code, 302)

        # Verify the note was updated
        updated_note = StickyNote.objects.get(id=self.note.id)
        self.assertEqual(updated_note.title, 'Updated Note')
        self.assertEqual(updated_note.content, 'This is an updated note.')

    def test_view_note_view(self):
        # Test viewing a specific note
        url = reverse('view_note', args=[self.note.id])
        response = self.client.get(url)
        # Check sucess response
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'view_note.html')
        # Check that the note details are displayed
        self.assertContains(response, 'Example Note')

    def test_delete_note_view(self):
        # Test deleting a note
        url = reverse('delete_note', args=[self.note.id])
        response = self.client.post(url)
        # Check page is redirected
        self.assertEqual(response.status_code, 302)

        # Verify the note was deleted
        with self.assertRaises(StickyNote.DoesNotExist):
            StickyNote.objects.get(id=self.note.id)

    def test_register_view(self):
        # Test user registration
        response = self.client.post(reverse('register_user'), {
            'username': 'newuser',
            'password1': 'complexpassword123',
            'password2': 'complexpassword123'
        })
        # Check page is redirected
        self.assertEqual(response.status_code, 302)

        # Verify the user was created
        new_user = User.objects.get(username='newuser')
        self.assertIsNotNone(new_user)

    def test_login_view(self):
        # Test user login
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpassword'
        })
        # Check page is redirected
        self.assertEqual(response.status_code, 302)

        # Check the user is authenticated
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_logout_view(self):
        # Test user logout
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)

        # Check the user is logged out
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_about_view(self):
        # Test the about view
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_contact_view(self):
        # Test the contact view
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
