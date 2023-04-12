from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    currency_num = currency()

    return render(request, 'index.html', context={
        'currency_num': currency_num}
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