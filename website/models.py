from django.db import models

# Create your models here.

class Newsletters(models.Model):
    email = models.EmailField()
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Newsletters'
        verbose_name_plural = 'Newsletterss'


class configuration(models.Model):
    description_newsletters = models.TextField()
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.description_newsletters

    class Meta:
        verbose_name = 'configuration'
        verbose_name_plural = 'configurations'


class Website(models.Model):
    nom_site = models.CharField(max_length=200)
    copyrigths = models.CharField(max_length=200)
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.nom_site

    class Meta:
        verbose_name = 'Website'
        verbose_name_plural = 'Websites'

class Lien_sociaux(models.Model):
    nom = models.CharField(max_length=200)
    icone = models.FileField(upload_to='image_site')
    liens = models.TextField()
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = 'Lien_sociaux'
        verbose_name_plural = 'Lien_sociauxs'