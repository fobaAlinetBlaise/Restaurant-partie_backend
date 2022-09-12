from .models import *
from rest_framework.viewsets import ModelViewSet
from .serializers import *
# from rest_framework.permissions import IsAuthenticated
# from rest_framework import filters

class ProfilModelViewSet(ModelViewSet):
    queryset = Profil.objects.prefetch_related('utilisateur')
    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return ReadProfilSerialiser
        return WriteProfilSerialiser
    # partie permettant l'authentification avant l'accès
    # permission_classes = (IsAuthenticated, )
    # # partie permettant de faire de filtre
    # filterset_fields = ['utilisateur', 'status', 'addresse']
    # # partie permettant de faire de recherche
    # search_fields = ['addresse']

class PlatCategorieModelViewSet(ModelViewSet):
    queryset = PlatCategorie.objects.all()
    def get_serializer_class(self):
        return PlatCategorieSerialiser
    # permission_classes = (IsAuthenticated, )
    
    
    
    
    
class NewslettersModelViewSet(ModelViewSet):
    queryset = Newsletters.objects.all()
    def get_serializer_class(self):
        return NewslettersSerialiser
    # permission_classes = (IsAuthenticated, )
    
    
    
class PlatModelViewSet(ModelViewSet):
    queryset = Plat.objects.prefetch_related('platcategorie')
    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return ReadPlatSerialiser
        return WritePlatSerialiser
    # permission_classes = (IsAuthenticated, )

class CommandeModelViewSet(ModelViewSet):
    queryset = Commande.objects.prefetch_related('utilisateur', 'plat')
    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return ReadCommandeSerialiser
        return WriteCommandeSerialiser
    # permission_classes = (IsAuthenticated, )

class BlogCategorieModelViewSet(ModelViewSet):
    queryset = BlogCategorie.objects.all()
    def get_serializer_class(self):
        return BlogCategorieSerialiser 
    # permission_classes = (IsAuthenticated, )                                
    
    

class BlogModelViewSet(ModelViewSet):
    queryset = Blog.objects.prefetch_related('utilisateur')
    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return ReadBlogSerialiser
        return WriteBlogSerialiser
    # permission_classes = (IsAuthenticated, )
    
    

class BlogCommentaireModelViewSet(ModelViewSet):
    queryset = BlogCommentaire.objects.prefetch_related('blog')
    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return ReadBlogCommentaireSerialiser
        return WriteCommentaireSerialiser
    # permission_classes = (IsAuthenticated, )
    

class EquipeModelViewSet(ModelViewSet):
    queryset = Equipe.objects.prefetch_related('utilisateur')
    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return ReadEquipeSerialiser
        return WriteEquipeSerialiser
    # permission_classes = (IsAuthenticated, )




class ContactModelViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    def get_serializer_class(self):
        return ContactSerialiser 
    # permission_classes = (IsAuthenticated, )
    
    
    
class GalleryVideoModelViewSet(ModelViewSet):
    queryset = GalleryVideo.objects.all()
    def get_serializer_class(self):
        return GalleryVideoSerialiser 
    # permission_classes = (IsAuthenticated, )
    

class GalleryPhotoModelViewSet(ModelViewSet):
    queryset = GalleryPhoto.objects.all()
    def get_serializer_class(self):
        return GalleryPhotoSerialiser
    # permission_classes = (IsAuthenticated, )


class TemoignageModelViewSet(ModelViewSet):
    queryset = Temoignage.objects.all()
    def get_serializer_class(self):
        return TemoignageSerialiser
    # permission_classes = (IsAuthenticated, )
    

class PartenaireModelViewSet(ModelViewSet):
    queryset = Partenaire.objects.all()
    def get_serializer_class(self):
        return PartenaireSerialiser
    # permission_classes = (IsAuthenticated, )
    

class AbonneModelViewSet(ModelViewSet):
    queryset = Abonne.objects.all()
    def get_serializer_class(self):
        return AbonneSerialiser
    # permission_classes = (IsAuthenticated, )