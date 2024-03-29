from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


class Service(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, unique=True)
    image = models.ImageField(upload_to="service_profile", default="default_service_profile.png", blank=True, null=True)
    desc = models.TextField(null=False, blank=False)
<<<<<<< HEAD
    email_address_associate = models.EmailField(null=True, blank=True)
    email_address_password = models.TextField(null=True, blank=True)
    receiver_email = models.TextField(null=True, blank=True)
=======
    email_address_associate = models.EmailField(null=False, blank=False)
    email_address_password = models.TextField(null=False, blank=False)
    receiver_email = models.TextField(null=False, blank=False)
>>>>>>> b372cbee3ebc850d66aeeecb2c6b25ea7a7f2d4d
    email_text_to_send_user = models.TextField(null=False, blank=False, default="Its that simple! You will be contacted by a qualified professional right away!")

    def __str__(self):
        return self.title

class Lead(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list


    name = models.CharField(max_length=300, null=False, blank=False)
    email_address = models.EmailField(null=False, blank=False)
    desc = models.TextField(null=False, blank=False)
    service_related = models.ForeignKey(Service, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.name


class NewsLetterEmail(models.Model):
    email_address = models.EmailField(null=False, blank=False)

    def __str__(self):
        return self.email_address



