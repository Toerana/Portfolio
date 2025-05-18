from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _

class Values(models.Model):
    prise = models.CharField(max_length=40)
    etat = models.BooleanField()

    def toggle_state(self):
        self.etat = not self.etat
        self.save()
    def all_on(self):
        self.etat = 1
        self.save()
    def all_off(self):
        self.etat = 0
        self.save()
class User(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name='webapp_user_set',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='webapp_user_set',
    )
