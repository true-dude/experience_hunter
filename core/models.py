from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.conf import settings

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)


class Topic(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    categories = models.ManyToManyField(Category, related_name='topics')


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class Feedback(models.Model):
    """Отзыв о прекрасном месте"""
    location_name = models.CharField(verbose_name='Название локации', max_length=100)
    description = models.CharField(verbose_name='Описание локации', max_length=5000)
    city = models.CharField(verbose_name='Город (Ближайший город', max_length=100)
    way = models.CharField(verbose_name='Как добраться (детали проезда/прохода до места)', max_length=5000)
    img = models.ImageField(verbose_name='Фото локации')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)