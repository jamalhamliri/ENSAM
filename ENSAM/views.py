from django.http import HttpResponseRedirect, HttpResponse

from django.shortcuts import render, redirect

from app.models import *


def ent(request):
    url = 'https://ent.univh2c.ma/uPortal/f/welcome/normal/render.uP'

    return HttpResponseRedirect('https://ent.univh2c.ma/uPortal/f/welcome/normal/render.uP')


def mooc_universite(request):
    return HttpResponseRedirect('http://www.mooc.univh2c.ma/')


def biblio(request):
    return HttpResponseRedirect('http://bums.univcasa.ma/')


def home(request):
    return redirect('/index/')


# def lire_pdf(request):
#     file_path = os.path.join(settings.STATIC_ROOT, 'assets', 'reglement.pdf')
#     return render(request, 'redirect.html', {'file_path': file_path})


def index(request):
    slide = Slide.objects.all()
    print(slide)
    # type=Article_type.objects.filter(name='Communiqués Officiels')
    # com_off = Article.objects.filter(Article_type_id=type)
    return render(request, 'index.html', {'slide': slide})


def afficher(request, article_id):
    article = Article.objects.filter(id=article_id)
    return render(request, 'afficher.html', {'article': article})


def api(request):
    return render(request, 'formation/prepa/api.html')


def GE(request):
    return render(request, 'formation/ing/GE.html')


def GM(request):
    return render(request, 'formation/ing/GM.html')


def MSE(request):
    return render(request, 'formation/ing/MSE.html')


def IAGI(request):
    return render(request, 'formation/ing/IAGI.html')


def CIME(request):
    return render(request, 'formation/Master/CIME.html')


def GCBCM(request):
    return render(request, 'formation/Master/GCBCM.html')


def MITD(request):
    return render(request, 'formation/Master/MITD.html')


def AISE(request):
    return render(request, 'formation/Licence/AISE.html')


def CSAA(request):
    return render(request, 'formation/Licence/CSAA.html')


def DI(request):
    return render(request, 'formation/Licence/DI.html')


def DLSS(request):
    return render(request, 'formation/Licence/DLSS.html')


def DWM(request):
    return render(request, 'formation/Licence/DWM.html')


def GC(request):
    return render(request, 'formation/Licence/GC.html')


def IDAMI(request):
    return render(request, 'formation/Licence/IDAMI.html')


def MSI(request):
    return render(request, 'formation/Licence/MSI.html')


def QSE(request):
    return render(request, 'formation/Licence/QSE.html')


def TTS(request):
    return render(request, 'formation/Licence/TTS.html')
