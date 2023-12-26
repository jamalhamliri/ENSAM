from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

from .views import *

admin.autodiscover()

urlpatterns = [
    path("sitemap.xml", sitemap, {"sitemaps": {"cmspages": CMSSitemap}}),
    path('en/etudiant/ent/', ent, name='external_redirect'),
    path('en/ent/', ent, name='external_redirect'),
    path('en/e-learning/mooc-universite-hassan-2/', mooc_universite, name='mooc_universite'),
    path('en/bibliotheque/', biblio, name='biblio'),
    path('en/index/', index, name='index'),
    path('en/afficher/<int:article_id>', afficher, name='afficher'),
    path('en/', home, name='afficher'),
    path('en/formation/prepa/', api, name='api'),
    path('en/formation/ing/ge/', GE, name='ge'),
    path('en/formation/ing/gm/', GM, name='gm'),
    path('en/formation/ing/iagi/', IAGI, name='iagi'),
    path('en/formation/ing/mse/', MSE, name='mse'),
    path('en/formation/master/cime/', CIME, name='cime'),
    path('en/formation/master/gcbcm/', GCBCM, name='gcbcm'),
    path('en/formation/master/mitd/', MITD, name='mitd'),
    path('en/formation/licence/aise', AISE, name='aise'),
    path('en/formation/licence/csaa', CSAA, name='csaa'),
    path('en/formation/licence/di', DI, name='di'),
    path('en/formation/licence/dlss', DLSS, name='dlss'),
    path('en/formation/licence/dwm', DWM, name='dwm'),
    path('en/formation/licence/gc', GC, name='gc'),
    path('en/formation/licence/idami', IDAMI, name='idami'),
    path('en/formation/licence/msi', MSI, name='msi'),
    path('en/formation/licence/qse', QSE, name='qse'),
    path('en/formation/licence/tts', TTS, name='tts'),

]

urlpatterns += i18n_patterns(path("admin/", admin.site.urls), path("", include("cms.urls")))

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
