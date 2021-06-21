from django.db import models

# Create your models here.






class Articles(models.Model):
    image = models.FileField(upload_to='image_site')
    prix = models.CharField(max_length =200)
    nom = models.CharField(max_length=200)
    categorie =  models.ForeignKey('categorie_articles', on_delete=models.CASCADE, related_name='categorie')
    marques =  models.ForeignKey('marques_articles', on_delete=models.CASCADE, related_name='marque')
    description = models.TextField()
    stock = models.BooleanField(default=True)
    quantite = models.IntegerField(default=True)
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)



    def __str__(self):
        return self.nom
    
    class Meta:
        verbose_name = 'Articles'
        verbose_name_plural = 'Articless'



class Categorie_articles(models.Model):
    nom = models.CharField(max_length=200)
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = 'Categorie_articles'
        verbose_name_plural = 'Categorie_articless'


class Marques_articles(models.Model):
    nom = models.CharField(max_length=200)
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = 'Marques_articles'
        verbose_name_plural = 'Marques_articless'



class Checkout(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=255)
    company = models.CharField(max_length=200)
    email = models.EmailField()
    pays = models.CharField(max_length=200)
    adresse = models.CharField(max_length=200)
    ville = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    code_postal = models.CharField(max_length=200)
    commentaire = models.TextField()
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)



    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Checkout'
        verbose_name_plural = 'Checkouts'
