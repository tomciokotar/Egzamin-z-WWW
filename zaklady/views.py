from django.shortcuts import render
from models import Mecz, Zaklad
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.datastructures import SortedDict

def glowna(request):
    mecze = Mecz.objects.all()
    wszystkiezaklady = []

    if 'zaznaczono' in request.POST:
        for zaklad in Zaklad.objects.all().order_by('mecz__opis', 'kto', 'wynika', 'wynikb'):
            if str(zaklad.mecz.id) in request.POST:
                wszystkiezaklady.append(zaklad)
    else:
        wszystkiezaklady = Zaklad.objects.all().order_by('mecz__opis', 'kto', 'wynika', 'wynikb')


    strona = request.POST.get('strona')
    paginator = Paginator(wszystkiezaklady, 10)

    try:
        zaklady = paginator.page(strona)
    except PageNotAnInteger:
        zaklady = paginator.page(1)
    except EmptyPage:
        zaklady = paginator.page(paginator.num_pages)

    wyniki = SortedDict()

    for zaklad in wszystkiezaklady:
        wyniki[zaklad.kto] = 0

    for zaklad in wszystkiezaklady:
        if zaklad.wynika == zaklad.mecz.wynika and zaklad.wynikb == zaklad.mecz.wynikb:
            wyniki[zaklad.kto] += 3
        elif zaklad.wynika == zaklad.wynikb and zaklad.mecz.wynika == zaklad.mecz.wynikb:
            wyniki[zaklad.kto] += 1
        elif zaklad.wynika > zaklad.wynikb and zaklad.mecz.wynika > zaklad.mecz.wynikb:
            wyniki[zaklad.kto] += 1
        elif zaklad.wynika < zaklad.wynikb and zaklad.mecz.wynika < zaklad.mecz.wynikb:
            wyniki[zaklad.kto] += 1


    slownik = {'zaklady': zaklady, 'wyniki': wyniki, 'mecze': mecze, 'wszystkiezaklady': wszystkiezaklady}
    return render(request, 'glowna.html', slownik)
