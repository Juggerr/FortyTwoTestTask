from django.db import models


class PersonalInfo(models.Model):

    name = models.CharField(
        "Name",
        max_length=255,
    )
    last_name = models.CharField(
        "Last name",
        max_length=255,
    )
    birth_date = models.DateField(
        "Date of birth",
        blank=True,
        null=True,
    )
    bio = models.TextField(
        "Biography",
        blank=True,
    )
    contacts = models.TextField(
        "Contacts",
        blank=True,
    )
    email = models.EmailField(
        "Email",
        blank=True,
    )
    jabber = models.CharField(
        "Jabber",
        max_length=128,
        blank=True,
    )
    skype = models.CharField(
        "Sjype",
        max_length=128,
        blank=True,
    )
    other = models.TextField(
        "Other contacts",
        blank=True,
    )

    def __str__(self):
        return "{} {}".format(self.name, self.last_name)
