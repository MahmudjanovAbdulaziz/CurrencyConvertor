from django.shortcuts import render
import requests



def index(request):
    respons = requests.get(url='https://api.exchangerate-api.com/v4/latest/USD').json()
    currenciens = respons.get('rates')

    if request.method == 'GET':


        context = {
            'currenciens' : currenciens
        }

        return render(request, 'currency_convert_app/index.html', context)

    if request.method == 'POST':
        from_amount = request.POST.get('amount')
        from_curr = request.POST.get('from_curr')
        to_curr = request.POST.get('to_curr')


        converted_amount = round((currenciens[to_curr] / currenciens[from_curr]) * float(from_amount), 2)

        context = {
            'currenciens' : currenciens,
            'converted_amount' : converted_amount,
            'from_curr' : from_curr,
            'to_curr' : to_curr
        }

        return render(request, 'currency_convert_app/index.html', context)

