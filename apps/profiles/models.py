from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from apps.common.models import TimeStampedUUIDModel

User = get_user_model()

#### List of American States

STATE_CHOICES = (('AL', 'Alabama'), ('AK', 'Alaska'), ('AS', 'American Samoa'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('AA', 'Armed Forces Americas'), ('AE', 'Armed Forces Europe'), ('AP', 'Armed Forces Pacific'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('MP', 'Northern Mariana Islands'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VI', 'Virgin Islands'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'))



class Profile(TimeStampedUUIDModel):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    phone_number = PhoneNumberField(
        verbose_name=_("Phone Number"), max_length=30, default="1(312)555-1212"
    )
    about_me = models.TextField(
        verbose_name=_("About me"), default="say something about yourself"
    )
    license = models.CharField(
        verbose_name=_("Real Estate license"), max_length=20, blank=True, null=True
    )
    profile_photo = models.ImageField(
        verbose_name=_("Profile Photo"), default="/profile_default.png"
    )

    country = CountryField(
        verbose_name=_("Country"), default="US", blank=False, null=False
    )
    city = models.CharField(
        verbose_name=_("City"),
        max_length=180,
        default="Chicago",
        blank=False,
        null=False,
    )
    state = models.CharField(
        verbose_name=_("State"),
        choices=STATE_CHOICES,
        max_length=18,
        default="IL",
        blank=False,
        null=False,
    )
    
    zipcode = models.CharField(
        verbose_name=_("Zip Code"),
        max_length=10,
        default="60625",
        blank=False,
        null=False,
    )
    is_buyer = models.BooleanField(
        verbose_name=_("Buyer"),
        default=False,
        help_text=_("Are you looking to Buy a Property?"),
    )
    is_seller = models.BooleanField(
        verbose_name=_("Seller"),
        default=False,
        help_text=_("Are you looking to sell a property?"),
    )
    is_agent = models.BooleanField(
        verbose_name=_("Agent"), default=False, help_text=_("Are you an agent?")
    )
    top_agent = models.BooleanField(verbose_name=_("Top Agent"), default=False)
    rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    num_reviews = models.IntegerField(
        verbose_name=_("Number of Reviews"), default=0, null=True, blank=True
    )

    def __str__(self):
        return f"{self.user.username}'s profile"
