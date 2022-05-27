from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def analyze(request):
    your_name = request.GET.get('your_name')
    their_name = request.GET.get('their_name')
    total_name = your_name.lower() + their_name.lower()

    count_t = total_name.count('t')
    count_r = total_name.count('r')
    count_u = total_name.count('u')
    count_e = total_name.count('e')
    count_l = total_name.count('l')
    count_o = total_name.count('o')
    count_v = total_name.count('v')

    pre_love_score = int(str(count_t+count_r+count_u+count_e)+str(count_l+count_o+count_v+count_e))
    love_score = pre_love_score%100
    params = {'love_score': love_score}
    return render(request, 'analyze.html', params)