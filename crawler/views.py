from django.shortcuts import render
from collections import OrderedDict
from operator import getitem

from . import scaper_python

def main_page(request):
    # dict_data = {1: {'name': 'APPLE iPhone 11 (Black, 128 GB)', 'price': '₹46,990', 'rating': '4.6', 'link': 'flipkart.com/apple-iphone-11-black-128-gb/p/itm8244e8d955aba?pid=MOBFWQ6BKRYBP5X8&lid=LSTMOBFWQ6BKRYBP5X8IBG6BS&marketplace=FLIPKART&q=iphone&store=tyy%2F4io&srno=s_1_1&otracker=AS_Query_TrendingAutoSuggest_8_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_8_0_na_na_na&fm=organic&iid=07715227-f7cc-4986-a4c7-f177b45da8cf.MOBFWQ6BKRYBP5X8.SEARCH&ppt=None&ppn=None&ssid=9sjljr8mw00000001666867585256&qH=0b3f45b266a97d70'}}
    dict_data = {}
    search_item = ''
    if request.method == 'GET':
        print(request.GET.__str__())
        _search_item = request.GET.get("searchItem", "")
        search_item = _search_item
        _sort_by = request.GET.get("sort")
        print(_search_item)
        print(_sort_by)
        dict_data = scaper_python.extract_all_data(_search_item)
        dict_data = OrderedDict(sorted(dict_data.items(), key=lambda x: getitem(x[1], _sort_by)))
        dict_data = {k: v for k, v in dict_data.items()}
    if request.method == 'POST':
        search_item = request.POST['search-input']
        dict_data = scaper_python.extract_all_data(search_item)
    return render(request, 'main_search.html', {'data': dict_data, 'searchItem': search_item})


def sorted_data(request):
    pass


# def search(request):
#     if request.method == "POST":
#         searched = request.POST['search']
#         print(searched)
#         return searched
