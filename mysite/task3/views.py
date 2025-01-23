# from django.views.generic import TemplateView
from django.shortcuts import render


def home_page(request):
    name_shop = 'RollShop'
    text_home_page = 'Главная страница'
    text_roll_sets = 'Наборы роллов'
    text_basket = 'Корзина'
    context = {'name_shop': name_shop,
               'text_home_page': text_home_page,
               'text_roll_sets': text_roll_sets,
               'text_basket': text_basket,
               }
    return render(request, 'roll_shop.html', context)


def roll_sets(request):
    name_page = 'roll_sets'
    text_name_page = 'Наборы роллов'
    text_sets_1 = 'Сет Азия'
    text_sets_2 = 'Сет Дракон'
    text_sets_3 = 'Сет Камикадзе'
    button_1 = 'Купить'
    button_2 = 'Вернуться обратно'
    context = {'name_page': name_page,
               'text_name_page': text_name_page,
               'text_sets_1': text_sets_1,
               'text_sets_2': text_sets_2,
               'text_sets_3': text_sets_3,
               'button_1': button_1,
               'button_2': button_2,
               }
    return render(request, 'roll_sets.html', context)


def basket(request):
    name_page = 'basket'
    text_name_page = 'Корзина'
    text = 'Вы еще не добавили ни одного товара в корзину'
    go_page_roll_sets = 'Перейти в меню'
    context = {'name_shop': name_page,
               'text_home_page': text_name_page,
               'text': text,
               'go_page_roll_sets': go_page_roll_sets,
               }
    return render(request, 'basket.html', context)
