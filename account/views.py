from wsgiref.util import request_uri
from django.http import HttpResponse
from django.shortcuts import render, redirect
from account.forms import FormConvert
from account.models import UserPersona
from .coba_pos_tagging import postag
#import nltk
#from nltk.stem import SnowballStemmer

def welcome(request):
    return render(request, 'account/welcome.html')
def login(request):
    return render(request, 'account/login.html')
def register(request):
    return render(request, 'account/register.html')
def result(request):
    return render(request, 'account/result.html')
def preview(request):
    return render(request, 'account/preview.html')

def history(request) :
    raw_results = UserPersona.objects.all()
    results = []
    for result in raw_results:
        res_postag = postag(result.needs, result.goals)
        results.append({
            "date": result.date,
            "nama": result.nama,
            "postag": res_postag
        })
    konteks = {
        'results' : results,
    }
    return render(request, 'account/history.html', konteks)

def preview(request):
    last_object= UserPersona.objects.last()
    context= {'last': last_object}
    return render(request, 'account/preview.html', context)

def tambah_data(request) :
    if request.POST:
        form = FormConvert(request.POST)
        if form.is_valid():
            form.save()
            form = FormConvert()
            pesan = "Data berhasil disimpan"
            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'account/preview.html', konteks)
    else:
        form = FormConvert()
        konteks = {
            'form': form,
        }
        return render(request, 'account/add-data.html', konteks)