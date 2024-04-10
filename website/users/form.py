from django.contrib.auth.forms import UserCreationForm
from   django.contrib.auth import get_user_model


class RegisterUserFormRecruter(UserCreationForm):
    model=get_user_model()
    fields=['nom','prenom','entreprise','login','pass','repass']

class RegisterUserFormCandidat(UserCreationForm):
    model=get_user_model()
    fields=['nom','prenom','login','pass','repass']