from django.shortcuts import render, redirect
from .models import Thinners, Im, Ukr_thinners, News, Order, Feedback
from .forms import OrderForm, FeedbackForm


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def thinners(request):
    thinners = Thinners.objects.all()
    img = Im.objects.all()
    context = {'thinners': thinners, 'img': img}
    return render(request, 'thinners.html', context=context)


def ukrthinners(request):
    ukrthinners = Ukr_thinners.objects.all()
    img = Im.objects.all()
    context = {'ukrthinners': ukrthinners, 'img': img}
    return render(request, 'ukr_thinners.html', context=context)


def news(request):
    news = News.objects.all()
    context = {'news': news}
    return render(request, 'news.html', context=context)


def get_thinner(request, thinner_pk):
    thinner = Thinners.objects.get(pk=thinner_pk)
    thinners = Thinners.objects.filter(pk=thinner_pk)
    context = {'thinners': thinners, 'thinner': thinner, }
    return render(request, 'thinner.html', context=context)


def get_ukrthinner(request, ukrthinner_pk):
    ukrthinner = Ukr_thinners.objects.get(pk=ukrthinner_pk)
    ukrthinners = Ukr_thinners.objects.filter(pk=ukrthinner_pk)
    context = {'ukrthinners': ukrthinners, 'ukrthinner': ukrthinner, }
    return render(request, 'ukrthinner.html', context=context)


def get_news(request, new_pk):
    new = News.objects.get(pk=new_pk)
    news = News.objects.filter(pk=new_pk)
    context = {'news': news, 'new': new, }
    return render(request, 'new.html', context=context)


def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            Order.objects.create(**form.cleaned_data)
            return redirect('index')
    else:
        form = OrderForm()
    return render(request, 'order.html', {'form': form})


def contacts(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            Feedback.objects.create(**form.cleaned_data)
            return redirect('index')
    else:
        form = FeedbackForm()
    return render(request, 'contacts.html', {'form': form})
