from django.contrib import admin
from django.urls import path, include
from Restaurant_app import views
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router = routers.SimpleRouter()
router.register(r'plat', views.PlatModelViewSet, basename='plat')
router.register(r'profil', views.ProfilModelViewSet, basename='profil')
router.register(r'platcategorie', views.PlatCategorieModelViewSet, basename='platcategorie')
router.register(r'commande', views. CommandeModelViewSet, basename='commande')
router.register(r'blogcategorie', views. BlogCategorieModelViewSet, basename='blogcategorie')
router.register(r'blogs', views.BlogModelViewSet, basename='blogs')
router.register(r'letters', views.NewslettersModelViewSet, basename='letters')
router.register(r'blogcommentaire', views. BlogCommentaireModelViewSet, basename='blogcommentaire')
router.register(r'equipe', views. EquipeModelViewSet, basename='equipe')
router.register(r'contact', views.ContactModelViewSet, basename='contact')
router.register(r'video', views. GalleryVideoModelViewSet, basename='video')
router.register(r'temoignage', views. TemoignageModelViewSet, basename='temoignage')
router.register(r'partenaire', views. PartenaireModelViewSet, basename='partenaire')
router.register(r'abonne', views. AbonneModelViewSet, basename='abonne')
router.register(r'photo', views. GalleryPhotoModelViewSet, basename='photo')


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
    # path('dj-rest-auth/', include('dj_rest_auth.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)