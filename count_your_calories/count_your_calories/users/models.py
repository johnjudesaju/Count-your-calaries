from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models


class User(AbstractUser):
    """
    Default custom user model for count your calories.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True,null=True,max_length=255)
    username = models.CharField(_("Enter username"),unique=True)
    email=models.EmailField(_("Enter Email"),unique=True)
    password=CharField(_("Enter password"),unique=True)
    role_choices=[("customer","customer"),("delivery","delivery")]
    role=models.CharField(_("Enter role"),choices=role_choices,null=False,blank=False,default="Admin")


    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
