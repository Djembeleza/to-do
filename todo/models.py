from django.db import models
import uuid
from django.contrib.auth.models import (AbstractBaseUser,
                                        PermissionsMixin)
from django.core.mail import send_mail
from django.conf import settings
from .managers import MyUserManager
from django.core.validators import validate_image_file_extension
# Create your models here.


class ToDo(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    title = models.CharField('To Do Title', max_length=50, blank=False)
    is_completed = models.BooleanField(default=False)
    todoDate = models.DateField('Due Date', blank=False)
    todoNote = models.TextField('Note')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    def note_summary(self):
        return self.todoNote[:15] + '...'

    class Meta:
        verbose_name = 'todo'
        verbose_name_plural = 'todos'
        ordering = ['todoDate']


class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("Email Address", max_length=254, unique=True)
    first_name = models.CharField('First Name', max_length=30, blank=True)
    last_name = models.CharField("Last Name", max_length=50, blank=True)
    # date_of_birth = models.DateField(blank=True)
    date_joined = models.DateField('Date Joined', auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='avatars/', null=True,
                               blank=True, validators=[validate_image_file_extension])

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.email

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email], **kwargs)
