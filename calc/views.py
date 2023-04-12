from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    currency_num = currency()

    return render(request, 'index.html', context={
        'currency_num': currency_num}
    )

def currency():
    return 5,5