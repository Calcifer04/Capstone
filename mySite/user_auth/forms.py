from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Registration details class model.
class SignupForm(UserCreationForm):
    """Class model for signup form with username, password and password reconfirmation fields.
    :param UserCreationForm: Inheritance of the django form class
    """
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
