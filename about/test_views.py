from django.urls import reverse
from django.test import TestCase
from .forms import CollaborateForm
from .models import About

class TestAboutViews(TestCase):

    def setUp(self):
        self.about_content = About(
            title="About Me", content="This is about me", 
        )
        self.about_content.save()

    def test_render_about_page_with_collabrate_form(self):
        response = self.client.get(reverse('about'))

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"About Me", response.content)
        self.assertIn(b"This is about me", response.content)
        self.assertIsInstance(response.context['collaborate_form'], CollaborateForm)

    def test_successful_form_submission(self):
        """Test for sending a collaboration request"""
        post_data = {
            'name': 'Test',
            'email': 'test@test.com',
            'message': "Let's collaborate"
        }
        response = self.client.post(reverse('about'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Collaboration request received! I endeavour to respond within 2 working days.",
            response.content)
