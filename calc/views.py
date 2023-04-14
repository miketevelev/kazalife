from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Category, Product


class CategoryListView(generic.ListView):
    model = Category


def index(request):
    resultcome = request.GET['price']
    if not resultcome:
        resultcome = '1'

    currency_num = currency()
    categorys = Category.objects.all()
    products = Product.objects.all()

    return render(request, 'index.html', context={
        'currency_num': currency_num,
        'categorys': categorys,
        'products': products,
        'resultcome': resultcome,}
    )

def currency():
    import requests
    from bs4 import BeautifulSoup

    currency_sum = 0.0

    url = "https://cbr.ru/currency_base/daily/"
    data = requests.get(url).text
    soup = BeautifulSoup(data, 'html.parser')
    tables = soup.find_all('table')
    table = soup.find('table', class_='data')

    for row in table.tbody.find_all('tr'):
        columns = row.find_all('td')

        if (columns != []):
            code = columns[0].text.strip()
            letter = columns[1].text.strip()
            count = columns[2].text.strip()
            currency = columns[3].text.strip()
            number = columns[4].text.strip()

            if code == '398' and letter == 'KZT':
                currency_sum = number

    return currency_sum