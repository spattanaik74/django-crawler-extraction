from django.shortcuts import render
from django.http import JsonResponse
import json


dict_data = {1: {'name': "samsung 12", 'price': '40000', 'rating': '4.5', 'link': 'Amazon.com'},
             2: {'name': "samsung 14", 'price': '45000', 'rating': '4.1', 'link': 'Flipkart.com', 'link': 'Amazon.com'},
             3: {'name': 'Apple iPhone 12 (128GB) - Blue', 'price': '₹54,900', 'rating': '4.6', 'link': 'Amazon.com'},
             4: {'name': 'Apple iPhone 14 128GB Starlight', 'price': '₹79,900', 'rating': '4.4', 'link': 'Amazon.com'},
             5: {'name': 'Apple iPhone 12 (64GB) - Blue', 'price': '₹49,900', 'rating': '4.6', 'link': 'Amazon.com'},
             6: {'name': 'Apple iPhone 13 (128GB) - Blue', 'price': '₹66,900', 'rating': '4.6', 'link': 'Amazon.com'}}


def main_page(request):
    return render(request, 'main_search.html', {'data': dict_data})


def search(request):
    if request.method == "POST":
        searched = request.POST['search']
        print(searched)
        return render(request, 'basic.html', {'searched': searched})
