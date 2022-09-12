from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UtilisateurSerialiser(serializers.ModelSerializer):
    class Meta:
        model  = User
        exclude = ['groups', 'user_permissions']

class ReadProfilSerialiser(serializers.ModelSerializer):
    utilisateur = UtilisateurSerialiser()
    class Meta:
        model   = Profil
        fields  = '__all__'

class WriteProfilSerialiser(serializers.ModelSerializer):
    class Meta:
        model  = Profil
        fields = '__all__'



class PlatCategorieSerialiser(serializers.ModelSerializer):
    class Meta:
        model  = PlatCategorie
        fields = '__all__'


class NewslettersSerialiser(serializers.ModelSerializer):
    class Meta:
        model  = Newsletters
        fields = '__all__'
        
        
class ReadPlatSerialiser(serializers.ModelSerializer):
    platcategorie = PlatCategorieSerialiser()
    class Meta:
        model = Plat
        fields = '__all__'        


class WritePlatSerialiser(serializers.ModelSerializer):
    class Meta:
        model  = Plat
        fields = '__all__'



class ReadCommandeSerialiser(serializers.ModelSerializer):
    utilisateur = UtilisateurSerialiser()
    plat = ReadPlatSerialiser()
    class Meta:
        model = Commande
        fields = '__all__'        


class WriteCommandeSerialiser(serializers.ModelSerializer):
    class Meta:
        model  = Commande
        fields = '__all__'



class BlogCategorieSerialiser(serializers.ModelSerializer):
    class Meta:
        model  = BlogCategorie
        fields = '__all__'



class ReadBlogSerialiser(serializers.ModelSerializer):
    utilisateur = UtilisateurSerialiser()
    blogcategorie = BlogCategorieSerialiser()
    class Meta:
        model = Blog
        fields = '__all__'        


class WriteBlogSerialiser(serializers.ModelSerializer):
    class Meta:
        model  = Blog
        fields = '__all__'
        
        


class ReadBlogCommentaireSerialiser(serializers.ModelSerializer):
    blog = ReadBlogSerialiser()
    class Meta:
        model = BlogCommentaire
        fields = '__all__'        


class WriteCommentaireSerialiser(serializers.ModelSerializer):
    class Meta:
        model  = BlogCommentaire
        fields = '__all__'
        
        
 
 
 
class GalleryPhotoSerialiser(serializers.ModelSerializer):
    class Meta:
        model  = GalleryPhoto
        fields = '__all__'

 
        
        
class ReadEquipeSerialiser(serializers.ModelSerializer):
    utilisateur = UtilisateurSerialiser()
    class Meta:
        model = Equipe
        fields = '__all__'        


class WriteEquipeSerialiser(serializers.ModelSerializer):
    class Meta:
        model  = Equipe
        fields = '__all__'



class TemoignageSerialiser(serializers.ModelSerializer):
    class Meta:
        model  = Temoignage
        fields = '__all__'
        
        

class AbonneSerialiser(serializers.ModelSerializer):
    class Meta:
        model  = Abonne
        fields = '__all__'
        
        


class PartenaireSerialiser(serializers.ModelSerializer):
    class Meta:
        model  = Partenaire
        fields = '__all__'




class GalleryVideoSerialiser(serializers.ModelSerializer):
    class Meta:
        model  = GalleryVideo
        fields = '__all__'




class ContactSerialiser(serializers.ModelSerializer):
    class Meta:
        model  = Contact
        fields = '__all__'






