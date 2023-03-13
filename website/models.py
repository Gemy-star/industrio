from django.db import models
from solo.models import SingletonModel

# Create your models here.


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
