import email
from urllib import request
from django.db import models
from random import random
import secrets
import string
import random
import string
import secrets
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.text import slugify
import os

# Create your models here.

# def renomer_image(instance, filename):
#     upload_to = 'image/'
#     ext = filename.split('.')[-1]
#     if instance.user.username:
#         filename = "photo/{}.{}".format(instance.user.username, ext)
#     return os.path.join(upload_to, filename)


def random_string(num):
    res = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(num))
    return str(res)




USER_TYPE = (
    ('client','client'),
    ('administrateur','administrateur'),
)


class Profil(models.Model):
    utilisateur      = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    photo            = models.ImageField(upload_to='Profil/%Y/%m/', blank=True, null=True)
    addresse         = models.CharField(max_length=200, blank=True, null=True)
    description      = models.TextField(max_length=200, blank=True, null=True)
    telephone        = models.CharField(max_length=20, blank=True, null=True)
    user_type        = models.CharField(max_length=200, default='client', choices = USER_TYPE,  blank=False, null=False)
    date_ajout       = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_modif       = models.DateTimeField(auto_now=True, auto_now_add=False)
    status           = models.BooleanField(default=True)
        
    def __str__(self):
        return self.utilisateur.username


# sauvegarde automatiquement les infos lorsque on creer un superuser
@receiver(post_save, sender= User)
def create_user_profil(sender, instance, created, **kwargs):
    if created:
        if instance.is_superuser:
            Profil.objects.create(user = instance, user_type='administrateur')
        else:
            Profil.objects.create(user = instance)






class PlatCategorie(models.Model):
    nom          = models.CharField(max_length=200, blank=False, null=False)
    date_ajout   = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_modif   = models.DateTimeField(auto_now=True, auto_now_add=False)
    status       = models.BooleanField(default=True)
    slug         = models.SlugField(max_length=200, blank=True, null=True, editable=False, unique=False)

    def __str__(self):
        return self.nom

# permet de mettre de mettre (-) entre les mots
def create_cateorie_slug(instance, new_slug=None):
    slug=slugify(instance.nom)
    if new_slug is not None:
        slug = new_slug
    ourQuery = PlatCategorie.objects.filter(slug= slug)
    exists   = ourQuery.exists()
    if exists:
        new_slug = "%s-%s" % (slug, ourQuery.first().id)
        return create_cateorie_slug(instance, new_slug=new_slug)
    return slug

def presave_categorie(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_cateorie_slug(instance)
pre_save.connect(presave_categorie, sender=PlatCategorie)






class Plat(models.Model):
    nom          = models.CharField(max_length = 200,null=False, blank = False)
    prix         = models.IntegerField(default=0, null=False, blank = False)
    platcategorie    = models.ForeignKey(PlatCategorie, on_delete=models.CASCADE, blank=False, null=False)
    photo        = models.ImageField(upload_to='Plat/%Y/%m/', blank=False, null=False)
    description  = models.TextField(blank=False, null=False) 
    date_ajout   = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_modif   = models.DateTimeField(auto_now=True, auto_now_add=False)
    status       = models.BooleanField(default=True)
    slug         = models.SlugField(max_length=200, blank=True, null=True, editable=False, unique=False)

    def __str__(self):
        return self.nom

def create_plat_slug(instance, new_slug=None):
    slug=slugify(instance.nom)
    if new_slug is not None:
        slug = new_slug
    ourQuery = Plat.objects.filter(slug= slug)
    exists   = ourQuery.exists()
    if exists:
        new_slug = "%s-%s" % (slug, ourQuery.first().id)
        return create_plat_slug(instance, new_slug=new_slug)
    return slug

def presave_plat(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_plat_slug(instance)
pre_save.connect(presave_plat, sender=Plat)
 
 
 
 
PAYEMENT = (
    ('Cash','Cash'),
)
class Commande(models.Model):
    utilisateur     = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    plat            = models.ForeignKey(Plat, on_delete=models.CASCADE, blank=False, null=False)
    quantite        = models.IntegerField(default=1, blank=False, null=False)
    date_ajout      = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_modif      = models.DateTimeField(auto_now=True, auto_now_add=False)
    status          = models.BooleanField(default=True)
    ref             = models.CharField(max_length=200, blank=True, null=True)
    payement        = models.CharField(max_length=200, default='Cash', choices = PAYEMENT)

    def __str__(self):
        return self.utilisateur.username



class Newsletters(models.Model):
    email = models.EmailField(max_length=100, blank=False, null=False)



class BlogCategorie(models.Model):
    nom          = models.CharField(max_length=200, blank=False, null=False)
    date_ajout   = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_modif   = models.DateTimeField(auto_now=True, auto_now_add=False)
    status       = models.BooleanField(default=True)
    slug         = models.SlugField(max_length=200, blank=True, null=True, editable=False, unique=False)

    def __str__(self):
        return self.nom

def create_blogcategorie_slug(instance, new_slug=None):
    slug=slugify(instance.nom)
    if new_slug is not None:
        slug = new_slug
    ourQuery = BlogCategorie.objects.filter(slug= slug)
    exists = ourQuery.exists()
    if exists:
        new_slug = "%s-%s" % (slug, ourQuery.first().id)
        return create_blogcategorie_slug(instance, new_slug=new_slug)
    return slug
def presave_blogcategorie(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_blogcategorie_slug(instance)
pre_save.connect(presave_blogcategorie, sender=BlogCategorie)
 



class Blog(models.Model):
    utilisateur   = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    blogcategorie = models.ForeignKey(BlogCategorie, on_delete=models.CASCADE, blank=False, null=False)
    photo         = models.ImageField(upload_to='Blog/%Y/%m/', blank=True, null=True)
    nom           = models.CharField(max_length=200, blank=False, null=False)
    description   = models.TextField(blank=False, null=False)
    date_ajout    = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_modif    = models.DateTimeField(auto_now=True, auto_now_add=False)
    status        = models.BooleanField(default=True)
    slug          = models.SlugField(max_length=200, blank=True, null=True, editable=False, unique=False)

    def __str__(self):
        return self.nom

def create_blog_slug(instance, new_slug=None):
    slug=slugify(instance.nom)
    if new_slug is not None:
        slug = new_slug
    ourQuery = Blog.objects.filter(slug= slug)
    exists = ourQuery.exists()
    if exists:
        new_slug = "%s-%s" % (slug, ourQuery.first().id)
        return create_blog_slug(instance, new_slug=new_slug)
    return slug
def presave_blog(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_blog_slug(instance)
pre_save.connect(presave_blog, sender=Blog)
    




class BlogCommentaire(models.Model):
    blog        = models.ForeignKey(Blog, blank=False, null=False, on_delete=models.CASCADE, related_name='comment_blog')
    nom         = models.CharField(max_length=200, blank=False, null=False)
    message     = models.TextField(blank=False, null=False)
    date_ajout  = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_modif  = models.DateTimeField(auto_now=True, auto_now_add=False)
    status      = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nom
    
class GalleryPhoto(models.Model):
    nom          = models.CharField(max_length=255, blank=False, null=False)
    photo = models.ImageField(upload_to='GalleryPhoto/%Y/%m/', blank=True, null=True)
    date_ajout   = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_modif   = models.DateTimeField(auto_now=True, auto_now_add=False)
    status       = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nom
    
    class Meta:
        ordering = ['-date_ajout']   
    
    
    
    

class Equipe(models.Model):
    utilisateur = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    fonction    = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    date_ajout  = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_modif  = models.DateTimeField(auto_now=True, auto_now_add=False)
    status      = models.BooleanField(default=True)
    
    def __str__(self):
        return self.utilisateur.username
    




    

class Temoignage(models.Model):
    nom         =models.CharField(max_length=200, blank=False, null=False)
    photo       =models.ImageField(upload_to='Temoignage/%Y/%m/', blank=True, null=True)
    fonction    = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    date_ajout  = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_modif  = models.DateTimeField(auto_now=True, auto_now_add=False)
    status      = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nom
    
    
    
    
    
    
class Abonne(models.Model):
    email       = models.EmailField(max_length=255, unique=True, null= False, blank=False)
    date_ajout  = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_modif  = models.DateTimeField(auto_now=True, auto_now_add=False)
    status      = models.BooleanField(default=True)
    
    def __str__(self):
        return self.email
        
        
        

class Partenaire(models.Model):
    nom         =models.CharField(max_length=200, blank=False, null=False)
    logo       =models.ImageField(upload_to='Logo/%Y/%m/', blank=True, null=True)
    website   = models.URLField(max_length=200, blank=True, null=True)
    date_ajout  = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_modif  = models.DateTimeField(auto_now=True, auto_now_add=False)
    status      = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nom  






class Contact(models.Model):
    nom       = models.CharField(max_length=200, blank=False, null=False)
    email     = models.EmailField(max_length=250, blank=False, null=False)
    telephone = models.CharField(max_length=200, blank=False, null=False)
    sujet     = models.CharField(max_length=200, blank=False, null=True)
    message   = models.TextField(blank=False, null=False)
    date_ajout= models.DateTimeField(auto_now=False, auto_now_add=True)
    date_modif= models.DateTimeField(auto_now=True, auto_now_add=False)
    status    = models.BooleanField(default=False)

    def __str__(self):
        return self.nom




class GalleryVideo(models.Model):
    nom          = models.CharField(max_length=255, blank=False, null=False)
    lien_youtube = models.URLField(max_length=255, blank=False, null=False)
    date_ajout   = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_modif   = models.DateTimeField(auto_now=True, auto_now_add=False)
    status       = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nom
    
    class Meta:
        ordering = ['-date_ajout']