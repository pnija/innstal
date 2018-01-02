from django.db import models
from django.contrib.auth.models import User

# Create your models here.


USER_TYPE = (
    ('0', 'Admin'),
    ('1', 'General'),
    ('2', 'Business')
)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    phone = models.CharField('mobile number', max_length=15, blank=True, null=True)
    user_type = models.CharField(choices=USER_TYPE, max_length=1, default=1)
    avatar = models.ImageField(upload_to='avatar_directory_path/', null=True, blank=True)

    class Meta:
        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfiles'
