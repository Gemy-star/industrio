from django.db import models
from solo.models import SingletonModel
from django. urls import reverse
import bs4
# Create your models here.
from djmoney.models.fields import MoneyField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.utils.translation import gettext as _


class WebsiteInfo(SingletonModel):
    site_name = models.CharField(max_length=255, default='Industrio')
    email = models.EmailField(null=True, default='Industrio@Industrio.com')
    phone = models.CharField(max_length=255, default='966563315019')
    facebook_link = models.URLField(null=True)
    instagram_link = models.URLField(null=True)
    linkendin_link = models.URLField(null=True)
    youtube_link = models.URLField(null=True)
    address = models.TextField(null=True)

    def __str__(self):
        return "Websitre Info"

    class Meta:
        verbose_name = "Websitre Info"


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True)
    message = models.TextField(null=True)

    class Meta:
        verbose_name = ("Contact")
        verbose_name_plural = ("Contacts")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Contact_detail", kwargs={"pk": self.pk})


class Project(models.Model):
    name = models.CharField(null=True, blank=True, max_length=255)
    owner = models.CharField(null=True, blank=True, max_length=255)
    client = models.CharField(null=True, blank=True, max_length=255)
    location = models.CharField(null=True, blank=True, max_length=255)
    total_cost = MoneyField(
        max_digits=14, decimal_places=2, default_currency='SAR')
    period_from = models.DateField(null=True, blank=True)
    period_to = models.DateField(null=True, blank=True)
    scope = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="projects_images/",null=True , blank=True)
    image_webp = ImageSpecField(
        source="image", format="WEBP", options={"quality": 100})
    image_thumb_png = ImageSpecField(
        source="image",
        processors=[ResizeToFill(335, 225)],
        format="PNG",
        options={"quality": 90},
    )
    image_thumb_webp = ImageSpecField(
        source="image",
        processors=[ResizeToFill(335, 225)],
        format="WEBP",
        options={"quality": 90},
    )

    @property
    def get_title_beauty(self):
        return bs4.BeautifulSoup(self.name, features="html5lib").get_text()

    @property
    def get_scope_beauty(self):
        return bs4.BeautifulSoup(self.scope, features="html5lib").get_text()

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Project_detail", kwargs={"pk": self.pk})
