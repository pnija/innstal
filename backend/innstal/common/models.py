from django.db import models
from django.contrib.auth.models import User

# Create your models here.


USER_TYPE = (
    ('0', 'Admin'),
    ('1', 'General'),
    ('2', 'Business')
)

class Country(models.Model):
    name = models.CharField(max_length=45)
    code = models.CharField(max_length=45)

    def __str__(self):
        return "%s" % (self.name)

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'



class City(models.Model):
    name = models.CharField(max_length=45)
    code = models.CharField(max_length=45)
    state = models.ForeignKey('common.State')
    country = models.ForeignKey('common.Country')

    def __str__(self):
        return "%s" % (self.name)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'



class State(models.Model):
    name = models.CharField(max_length=45)
    code = models.CharField(max_length=45)
    country = models.ForeignKey('common.Country')

    def __str__(self):
        return "%s" % (self.name)

    class Meta:
        verbose_name = 'State'
        verbose_name_plural = 'States'


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField('mobile number', max_length=15, blank=True, null=True)
    user_type = models.CharField(choices=USER_TYPE, max_length=1, default=1)
    address = models.TextField(null=True, blank=True)
    city = models.ForeignKey(City, null=True, blank=True)
    state = models.ForeignKey(State, null=True, blank=True)
    country = models.ForeignKey(Country, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatar_directory_path/', null=True, blank=True)

    class Meta:
        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfiles'


class PricingPlan(models.Model):
    name = models.CharField('Package Name', max_length=50, unique=True)
    title = models.CharField('Package Title', max_length=50, blank=True, null=True)
    price = models.CharField('Package Cost', max_length=50)
    duration = models.DurationField(default=2000, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
