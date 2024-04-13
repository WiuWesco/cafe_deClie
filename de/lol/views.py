from django.shortcuts import render
from django.db import models
from . import models
from .forms import *
def main(request):
    data = models.for_main.objects.all()
    return render(request, 'index.html',{'data' : data})
def feedback(request):
    if request.method == 'POST':
        form = Forfeedback(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            sername = form.cleaned_data['sername']
            email = form.cleaned_data['email']
            text = form.cleaned_data['text']
            w2 = models.feedback()
            w2.name = name
            w2.sername = sername
            w2.email = email
            w2.text = text
            w2.save()
    else:
        form = Forfeedback()
    return render(request,'feedback.html',{'form' : form})
def galary(request):
    data = models.galary.objects.all()
    return render(request,'galary.html', {'data' : data})
def mp(request):
    data = models.MP.objects.all()
    return render(request,'mp.html', {'data' : data})
def infa_of_mp(request,num):
    if request.method == 'POST':
        form = ForMPForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            sername = form.cleaned_data['sername']
            email = form.cleaned_data['email']
            w2 = models.RegMP()
            w2.name = name
            w2.sername = sername
            w2.email = email
            w2.MP = num
            w2.save()
    else:
        form = ForMPForm()
    data = models.MP.objects.filter(title=num)
    return render(request,'infa_of_mp.html', {'data' : data[0],'form' : form})
def information(request):
    return render(request,'information.html')
def store(request):
    data = models.store.objects.all()
    return render(request,'store.html', {'data' : data})
def vacance(request):
    data = models.vacance.objects.all()
    return render(request,'vacance.html', {'data' : data})
def store_chapter(request,num):
    data = models.store_chapter.objects.filter(category=num)
    return render(request,'store_chapter.html', {'data' : data})
def reservation(request):
    form = ForReservation(request.POST)
    if form.is_valid():
        table = ""
        reservation = models.reservation()
        reservation.date = form.cleaned_data['date']
        reservation.name = form.cleaned_data['name']
        reservation.sername = form.cleaned_data['sername']
        reservation.number = form.cleaned_data['number']
        for i in range(10):
            if form.cleaned_data[str('table'+str(i + 1))]:
                table += str(i + 1) + ' '
        if table == '':
            return HttpResponse(status=404)
        reservation.place = table
        reservation.save()
    else:
        form = ForReservation(request.POST)
    return render(request,'reservation.html',{'form' : form})

#exec("%n.%s.%d" % ("models",num,"objects.all()"))
