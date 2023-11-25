from django.db import models
from ckeditor_uploader .fields import RichTextUploadingField
from django.db.models.signals import pre_save
from django.dispatch import receiver
import  requests
# Create your models here.
class Tag(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name
class Advantage(models.Model):
    title=models.CharField(max_length=200)
    poster=models.ImageField(upload_to="poster/")
    tags=models.ManyToManyField(Tag)
    body=RichTextUploadingField()
    def __str__(self):
        return self.title

class Course(models.Model):
    image=models.ImageField(upload_to="images/")
    name=models.CharField(max_length=200)
    order=models.IntegerField(default=1)
    body=RichTextUploadingField()



    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Author(models.Model):
    full_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="author_images/")
    position = models.CharField(max_length=200)

    def __str__(self):
        return self.full_name
class Article(models.Model):
    title=models.CharField(max_length=200)
    poster=models.ImageField(upload_to="images/")
    tags=models.ManyToManyField(Tag)
    created_at=models.DateField(auto_now_add=True,)
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True)
    body = RichTextUploadingField()
    author = models.ForeignKey(Author,
                               on_delete=models.SET_NULL,
                               null=True,
                               blank=True)

    def __str__(self):
        return self.title








class Gallery(models.Model):
    image=models.ImageField(upload_to="gallery_images/")
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Way2job(models.Model):
    title=models.CharField(max_length=100)
    body=RichTextUploadingField()

    def __str__(self):
        return self.title

class AplicationForm(models.Model):
    name=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=50)

    def __str__(self):
        return self.name
@receiver(pre_save,sender=AplicationForm)
def sent_to_telegram_bot(sender,instance,**kwargs):

    TOKEN="AAHC6oPHiKhyoX4u_og1GMsxY9Z7Gg1XMPA"
    CHAT_ID=5114332580
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    print(instance.phone_number)
    text=f""" Arizachining ismi :{instance.name}\n
    Telefon Raqami:{instance.phone_number}"""
    params={"chat_id":CHAT_ID,
            "text":text
            }
    requests.post(url=url,params=params)
