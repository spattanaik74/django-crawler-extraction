from django.shortcuts import render
from django.http import JsonResponse
import json


def main_page(request):
    return render(request, 'main_search.html')


def search(request):
    if request.method == "POST":
        searched = request.POST['search']
        print(searched)
        return render(request, 'basic.html', {'searched': searched})
