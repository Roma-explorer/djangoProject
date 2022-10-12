from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def test(request):
    s = request.POST.get('greeting')
    return JsonResponse({'returned': s.upper()})
