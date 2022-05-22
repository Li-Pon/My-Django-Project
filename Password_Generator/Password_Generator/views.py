import random
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def result(request):
    letter = request.GET.get('letter', '0')
    number = request.GET.get('number', '0')
    symbol = request.GET.get('symbol', '0')
    
    all_letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
    'q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J',
    'K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    all_number = ['0','1','2','3','4','5','6','7','8','9']
    all_symbol = ['.',',','?',';','!',':','(',')','{','}','[',']','_','-','/','@','#','$','%','^',
    '&','*','~']

    listing_password = []
    for let in range(int(letter)):
        listing_password.append(random.choice(all_letter))
    for num in range(int(number)):
        listing_password.append(random.choice(all_number))
    for sym in range(int(symbol)):
        listing_password.append(random.choice(all_symbol))
    
    random.shuffle(listing_password)

    generated_password = ""
    for i in listing_password:
        generated_password += i

    params = {'result':generated_password}
    return render(request, 'result.html', params)
