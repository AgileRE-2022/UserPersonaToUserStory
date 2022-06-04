from wsgiref.util import request_uri
from django.http import HttpResponse
from django.shortcuts import render
from account.forms import FormConvert
from account.models import UserPersona

def welcome(request):
    return render(request, 'account/welcome.html')
def login(request):
    return render(request, 'account/login.html')
def register(request):
    return render(request, 'account/register.html')
def result(request):
    return render(request, 'account/result.html')

def history(request) :
    results = UserPersona.objects.all()
    konteks = {
        'results' : results,
    }
    return render(request, 'account/history.html', konteks)

# def coba_fungsi(request):
#     print("HALO???????????????????????????")
#     return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")

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
            return render(request, 'account/add-data.html', konteks)
    else:
        form = FormConvert()
        konteks = {
            'form': form,
        }
        return render(request, 'account/add-data.html', konteks)