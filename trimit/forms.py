from django import forms
from django.contrib.auth.models import User
from trimit.models import UserProfile, Page, Review
from django_countries.widgets import CountrySelectWidget
from django.core.validators import RegexValidator


class ReviewForm(forms.ModelForm):
    atmosphere_rating=forms.FloatField(min_value=0, max_value=5)
    price_rating=forms.FloatField(min_value=0, max_value=5)
    service_rating=forms.FloatField(min_value=0, max_value=5)
    picture=forms.ImageField(required=False)
    comment=forms.CharField(required=False)

    class Meta:
        model = Review
        exclude = ('page', 'user', 'average_rating', 'time')


class UserRegisterForm(forms.ModelForm):
    # form used to save information for the User model
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # setting the attributes for the form fields
        self.fields['username'].widget.attrs.update({'id': 'username-field'})
        self.fields['email'].widget.attrs.update({'id': 'email-field',
                                                  'placeholder': 'e.g. user@trimit.com'},)
        self.fields['email'].required = True
        self.fields['password'].widget.attrs.update({'id': 'password-field'})
        self.fields['username'].label = 'Username*'
        self.fields['email'].label = 'Email*'
        self.fields['password'].label = 'Password*'

    def clean_email(self):
        # making sure the email provided is unique
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return email


class UserEditForm(UserRegisterForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.HiddenInput()


class HairdresserPageForm(forms.ModelForm):
    # form used in order to save hairdresser page information based on the Page model
    # setting the opening_times field to use a text area widget
    opening_times = forms.CharField(max_length=300,
                                    required=False,
                                    widget=forms.Textarea(
                                        attrs={'placeholder': 'e.g.\n'
                                                              'Mon - Fri: 9:30am to 17:30pm\n'
                                                              'Closed on weekends',
                                               }
                                        ),
                                    )

    # setting the contact number up to be validated using a regex validator
    contact_number = forms.CharField(min_length=8,
                                     required=False,
                                     validators=[RegexValidator(r'^\+?1?\d{9,15}$',
                                                                message="Contact number must be 8 to 15 digits long "
                                                                        "and can have a leading '+'.")])


    class Meta:
        model = Page
        fields = ('name', 'flat_number', 'street_address', 'city', 'postcode', 'country', 'opening_times',
                  'contact_number', 'profile_picture', 'webpage', 'instagram', 'specialities')
        # setting the layout of the country select widget
        widgets = {'country': CountrySelectWidget(
            layout='<div class="country-widget">{widget}<img class="country-select-flag" id="{flag_id}" style="margin: 6px 0 0 4px" src="{country.flag}"></div>'
        )}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].label = 'Display name'
        self.fields['name'].widget.attrs.update({'id': 'name-field',
                                                 'placeholder': "e.g. Hairy Mary's"})
        self.fields['flat_number'].widget.attrs.update({'id': 'flat_number-field'})
        self.fields['street_address'].widget.attrs.update({'id': 'street_address-field',
                                                           'placeholder': 'e.g. 10 Bath Street'})
        self.fields['city'].widget.attrs.update({'id': 'city-field',
                                                 'placeholder': 'e.g. Glasgow'})
        self.fields['postcode'].widget.attrs.update({'id': 'postcode-field'})
        self.fields['country'].widget.attrs.update({'id': 'country-field'})
        self.fields['opening_times'].widget.attrs.update({'id': 'opening_times-field'})
        self.fields['contact_number'].widget.attrs.update({'id': 'contact_number-field'})
        self.fields['webpage'].widget.attrs.update({'id': 'webpage-field'})
        self.fields['instagram'].widget.attrs.update({'id': 'instagram-field'})

        self.fields['street_address'].label = 'Street address*'
        self.fields['city'].label = 'City*'
        self.fields['country'].label = 'Country*'
        self.fields['opening_times'].required = False


class HairPageSpecialityForm(forms.ModelForm):
    # form used for the search page in order to render the proper tags field
    class Meta:
        model = Page
        fields = ('specialities', )

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['specialities'].label = 'Hair Specialities'


class UserProfileForm(forms.ModelForm):
    # form used in order to obtain the profile picture for a userprofile on user registration
    class Meta:
        model = UserProfile
        fields = ('profile_picture',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profile_picture'].widget.attrs.update({'id': 'profile-picture-field'})

