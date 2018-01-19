from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


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
    state = models.ForeignKey('common.State', null=True, blank=True)
    country = models.ForeignKey('common.Country', null=True, blank=True)

    def __str__(self):
        return "%s" % (self.name)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'


class State(models.Model):
    name = models.CharField(max_length=45,null=True,blank=True)
    code = models.CharField(max_length=45,null=True,blank=True)
    country = models.ForeignKey('common.Country', null=True)

    def __str__(self):
        return "%s" % (self.name)

    class Meta:
        verbose_name = 'State'
        verbose_name_plural = 'States'
        

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='get_user_profile')
    phone = models.CharField('mobile number', max_length=15, blank=True, null=True)
    user_type = models.CharField(choices=USER_TYPE, max_length=1, default=1)
    address = models.TextField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    city = models.ForeignKey(City, null=True, blank=True)
    state = models.ForeignKey(State, null=True, blank=True)
    country = models.ForeignKey(Country, null=True, blank=True)
    zipcode = models.CharField(max_length= 100,null= True, blank= True)
    avatar = models.ImageField(upload_to='avatar_directory_path/', null=True, blank=True)

    def __str__(self):
        return "%s" % (self.user.username)

    class Meta:
        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfiles'

    def __str__(self):
        return self.user.username

class BusinessUserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(choices=USER_TYPE, max_length=1, default=1)
    company_name = models.CharField(max_length= 100,null= True, blank= True)
    phone = models.CharField('mobile number', max_length=15, blank=True, null=True)
    person_to_contact = models.CharField(max_length= 100,null= True, blank= True)
    address = models.TextField(null=True, blank=True)
    city = models.ForeignKey(City, null=True, blank=True)
    state = models.ForeignKey(State, null=True, blank=True)
    country = models.ForeignKey(Country, null=True, blank=True)
    fax_number = models.CharField(max_length=100, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatar_directory_path/', null=True, blank=True)
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return "%s" % (self.user.username)


class PricingPlan(models.Model):
    name = models.CharField('Package Name', max_length=50, unique=True)
    title = models.CharField('Package Title', max_length=50, blank=True, null=True)
    price = models.CharField('Package Cost', max_length=50)
    duration = models.DurationField(default=2000, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    blog_title = models.CharField(max_length=255, null=True, blank=True)
    blog_subtitle = models.CharField(max_length=255, null=True, blank=True)
    blog_image = models.ImageField(upload_to='blog_images_path/', null=True, blank=True)
    blog_content = RichTextField()

    def __str__(self):
        return self.blog_title


class UserPlans(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pricing_plan = models.ForeignKey(PricingPlan, on_delete=models.CASCADE)


class Newsletter(models.Model):
    email = models.EmailField(max_length=70, blank=False)
    is_subscribed = models.BooleanField(default=False)

    def __str__(self):
        return self.email
