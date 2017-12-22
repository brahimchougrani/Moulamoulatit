from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.forms import ModelForm, inlineformset_factory, modelformset_factory
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Circuit, CirctuiDetail, ImageUpload, Prisencharche, lesinfos
from PIL import Image


class Cicuitform(ModelForm):
    class Meta:
        model = Circuit
        exclude = ()


class CirctuiForm(ModelForm):
    class Meta:
        model = CirctuiDetail
        exclude =()


class PrisencharcheForm(ModelForm):
    class Meta:
        model = Prisencharche
        exclude =()

class FamilyMemberForm(ModelForm):
    class Meta:
        model = ImageUpload
        exclude = ()



class PhotoForm(forms.ModelForm):

    x = forms.FloatField(widget=forms.HiddenInput)
    y = forms.FloatField(widget=forms.HiddenInput)
    height = forms.FloatField(widget=forms.HiddenInput)
    width = forms.FloatField(widget=forms.HiddenInput)

    class Meta:
        model = ImageUpload
        fields = ('relationship', 'x','y','height','width',)

    def save(self,*args,**kwargs):
        photo = super(PhotoForm, self).save()

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')
        if x > 0 or x <= 0:
            if y>0 or y<=0:
                if w > 0 or w <= 0:
                    if h > 0 or h <= 0:
                        image = Image.open(photo.relationship)
                        cropped_image = image.crop((x, y, w+x, h+y))
                        resized_image = cropped_image.resize((500, 700), Image.ANTIALIAS)
                        resized_image.save(photo.relationship.path)
                        return super(PhotoForm, self).save(*args, **kwargs)




CircuitwithDetail = inlineformset_factory(Circuit, CirctuiDetail,form=CirctuiForm,extra=1)
CircuitwithPrisenCharge = inlineformset_factory(lesinfos, Prisencharche,form=PrisencharcheForm,extra=10)
FamilyMemberFormSet = inlineformset_factory(Circuit, ImageUpload,form=PhotoForm,extra=1)
