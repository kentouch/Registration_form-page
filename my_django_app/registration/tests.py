from django.test import TestCase
from .forms import RegistrationForm

class RegistrationFormTest(TestCase):
    def test_form_validity(self):
        form_data = {
            'delegate_category': 'Category 1',
            'firstname': 'John',
            'lastname': 'Doe',
            'email': 'john.doe@example.com',
            'nationality': 'Burundian',
            'national_id': '123456789',
            'phone_number': '1234567890',
            'address': '123 Main St',
            'organization': 'Example Org',
            'position': 'Member',
            'country_of_residence': 'Burundi',
            'social_activities': 'Activity 1',
        }
        form = RegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_email(self):
        form_data = {
            'delegate_category': 'Category 1',
            'firstname': 'John',
            'lastname': 'Doe',
            'email': 'invalid-email',
            'nationality': 'Burundian',
            'national_id': '123456789',
            'phone_number': '1234567890',
            'address': '123 Main St',
            'organization': 'Example Org',
            'position': 'Member',
            'country_of_residence': 'Burundi',
            'social_activities': 'Activity 1',
        }
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_form_missing_fields(self):
        form_data = {}
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 12)  # Assuming all fields are required