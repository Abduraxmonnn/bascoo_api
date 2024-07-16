from django.db import models


# Create your models here.


def image_upload_to(instance, filename):
    # file will be uploaded to MEDIA_ROOT/products/images/<title>/<filename>
    return 'products/images/{0}/{1}'.format(instance.title, filename)


def video_upload_to(instance, filename):
    # file will be uploaded to MEDIA_ROOT/products/images/<title>/<filename>
    return 'products/videos/{0}/{1}'.format(instance.title, filename)


class Product(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to=image_upload_to, null=True)
    video = models.FileField(upload_to=video_upload_to, null=True)
    description = models.TextField()
    is_public = models.BooleanField(default=False)

    created_date = models.DateField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Contact(models.Model):
    phone_1 = models.CharField(max_length=12, verbose_name='Phone number 1')
    phone_2 = models.CharField(max_length=12, verbose_name='Phone number 2')
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'


class EmailMessage(models.Model):
    name = models.CharField(max_length=255)
    sender = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.sender

    class Meta:
        verbose_name = 'Email Message'
        verbose_name_plural = 'Email Messages'
