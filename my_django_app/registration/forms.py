from django import forms

class RegistrationForm(forms.Form):
    DELEGATE_CATEGORIES = [
        ('category1', 'Category 1'),
        ('category2', 'Category 2'),
        ('category3', 'Category 3'),
    ]

    SOCIAL_ACTIVITIES = [
        ('activity1', 'Activity 1'),
        ('activity2', 'Activity 2'),
        ('activity3', 'Activity 3'),
    ]

    delegate_category = forms.ChoiceField(choices=DELEGATE_CATEGORIES, label='Delegate Category')
    firstname = forms.CharField(max_length=30, label='First Name')
    lastname = forms.CharField(max_length=30, label='Last Name')
    email = forms.EmailField(label='Email')
    nationality = forms.CharField(max_length=30, label='Nationality')
    national_id = forms.CharField(max_length=20, label='National ID')
    phone_number = forms.CharField(max_length=15, label='Phone Number')
    address = forms.CharField(widget=forms.Textarea, label='Address')
    organization = forms.CharField(max_length=50, label='Organization')
    position = forms.CharField(max_length=30, label='Position')
    country_of_residence = forms.CharField(max_length=30, label='Country of Residence')
    social_activities = forms.ChoiceField(choices=SOCIAL_ACTIVITIES, label='Social Activities')