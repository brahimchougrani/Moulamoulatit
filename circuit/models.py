from django.db import models

# Create your models here.
from django.urls import reverse


class Circuit(models.Model):
    Titre = models.CharField(max_length=255)
    Description = models.TextField(null=True)
    img = models.ImageField()
    def __str__(self):
        return self.Titre

    def get_absolute_url(self):
        return reverse('moulatitcircuit:CircuitDetail',kwargs={
            'pk':self.pk
        })

    def get_first_image(self):
        if self.imageupload_set.all().first():
            return self.imageupload_set.all().first().relationship.url
        else:
            return None

class CircuitParts(models.Model):
    titre_circuit = models.CharField(max_length=255)
    Description = models.TextField(null=True)
    class Meta:
        abstract = True

class CirctuiDetail(CircuitParts):
    Circuit = models.ForeignKey(Circuit)
    def __str__(self):
        return self.titre_circuit

class lesinfos(models.Model):
    titre = models.CharField(max_length=255)

    def __str__(self):
        return self.titre

class Prisencharche(CircuitParts):
    Infos = models.ForeignKey(lesinfos)

    def __str__(self):
        return self.titre_circuit

class ImageUpload(models.Model):
    relationship = models.ImageField(blank=False,null=False)
    x = models.FloatField(blank=False,null=False)
    y = models.FloatField(blank=False,null=False)
    width = models.FloatField(blank=False,null=False)
    height = models.FloatField(blank=False,null=False)
    bld = models.ForeignKey(Circuit, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return str(self.relationship)

    def get_img_url(self):
        return self.relationship.url()


class HomeDetail(models.Model):
    logo = models.ImageField()
    facebook = models.URLField()
    Instagram = models.URLField()
    Email = models.EmailField()
    Fax = models.IntegerField()
    Mobile = models.IntegerField()
    Adress = models.CharField(max_length=255)
    img_1 = models.ImageField(blank=True,null=True)
    description1 = models.TextField(blank=True,null=True)
    img_2 = models.ImageField(blank=True,null=True)
    description2 = models.TextField(blank=True,null=True)
    img_3= models.ImageField(blank=True,null=True)
    description3 = models.TextField(blank=True,null=True)
    histoire = models.TextField(blank=True,null=True)
    def __str__(self):
        return self.Adress



