import requests
from bs4 import BeautifulSoup
from operator import getitem
from collections import OrderedDict


def filpark_get_url(search_item):
    search_item = search_item.replace(' ', '+')
    link_flipkart = f'https://www.flipkart.com/search?q={search_item}&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_8_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_8_0_na_na_na&as-pos=8&as-type=TRENDING&suggestionId=tv&requestId=9c9fa553-b7e5-454b-a65b-bbb7a9c74a29'
    return link_flipkart


def amazon_get_url(search_item):
    search_item = search_item.replace(' ', '+')
    link_amazon = f'https://www.amazon.in/s?k={search_item}&crid=2TAD9MHWU8R6E&sprefix=iphone%2Caps%2C321&ref=nb_sb_noss_2'
    return link_amazon


def extract_model_flipkart(item):
    dict_data = {}

    page = requests.get(filpark_get_url(item))

    soup = BeautifulSoup(page.content, 'html.parser')
    count = 1
    for data in soup.findAll('div', class_='_2kHMtA'):
        dict_data[count] = {
            'name': data.find('div', attrs={'class': '_4rR01T'}).text,
            'price': data.find('div', attrs={'class': '_30jeq3 _1_WHN1'}).text.replace('₹', '').replace(',', ''),
            'rating': ["0" if not data.find('div', attrs={'class': '_3LWZlK'})
                       else data.find('div', attrs={'class': '_3LWZlK'}).text][0],
            'link': 'flipkart.com' + data.find('a', attrs={'class': '_1fQZEK'})['href']}

        count += 1

    return dict_data


def extract_model_amazon(item):
    HEADERS = ({'User-Agent':
                    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 '
                    'Safari/537.36',
                'Accept-Language': 'en-US'})
    dict_data = {}
    page = requests.get(amazon_get_url(item), headers=HEADERS)
    soup = BeautifulSoup(page.content, 'html.parser')
    count = 1
    for data in soup.findAll('div', class_='sg-col sg-col-4-of-12 sg-col-8-of-16 sg-col-12-of-20 s-list-col-right'):
        dict_data[count] = {
            'name': data.find('span', attrs={'class': 'a-size-medium a-color-base a-text-normal'}).text,
            'price': ["0" if not data.find('span', attrs={'class': 'a-price-whole'})
                            else data.find('span', attrs={'class': 'a-price-whole'}).text][0].replace(',', ''),
            'rating': ["0" if not data.find('span', attrs={'class': 'a-icon-alt'})
                       else data.find('span', attrs={'class': 'a-icon-alt'}).text][0][:3],
            'link': 'amazon.in' + data.find('a', attrs={
                'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})['href']}
        count += 1

    return dict_data


# _3pLy-c row

# model = extract_model_amazon('iphone')
# model2 = extract_model_flipkart('iphone')
# for v in model.values():
#     print(v)
# for v in model2.values():
#     print(v)

def extract_all_data(item):
    dict_all_data = {}
    count = 1
    for v in extract_model_amazon(item).values():
        dict_all_data[count] = v
        count += 1
    for v in extract_model_flipkart(item).values():
        dict_all_data[count] = v
        count += 1

    return dict_all_data
