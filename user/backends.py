
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from user.models import CustomUser

class EmailOrPhoneBackend(ModelBackend):

    def authenticate(self, request, email=None, password=None,backend='user.backends.EmailOrPhoneBackend', **kwargs):
        UserModel = CustomUser
        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            try:
                user = UserModel.objects.get(email=email)
            except UserModel.DoesNotExist:
                return None
        if user.check_password(password):
            return user
        return None