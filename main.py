# cook_book = {}
# with open('recipies.txt', 'rt', encoding='utf-8') as file:
#     dishes = ''
#     for dish in file:
#         dish = dish.strip()
#         if dish.isdigit():
#             continue
#         elif dish and '|' not in dish:
#             cook_book[dish] = []
#             dishes = dish
#         elif dish and '|' in dish:
#             a, b, c = dish.split(" | ")
#             cook_book.get(dishes).append(dict(ingredient_name=a, quantity=int(b), measure=c))
#
# print(cook_book)
#
# def get_shop_list_by_dishes(dishes_list, person_count):
#     shop_list = {}
#     for dish in dishes_list:
#         if dish in cook_book:
#             for ingredients in cook_book[dish]:
#                 if ingredients['ingredient_name'] in shop_list:
#                     shop_list[ingredients['ingredient_name']]['quantity'] += ingredients['quantity'] * person_count
#                 else:
#                     shop_list[ingredients['ingredient_name']] = ({'measure': ingredients['measure'], 'quantity':
#                                                                 (ingredients['quantity'] * person_count)})
#         else:
#             print('Такого блюда нет в меню')
#     return shop_list
# print(get_shop_list_by_dishes(['Омлет'], 2))
#
#
#
from pprint import pprint


def read_recipes():
    recipe = {}
    with open('recipies.txt', 'r', encoding='UTF-8') as f:
        line = f.readline().strip()
        while line != '':
            dish = line
            count_ingredients = int(f.readline().strip())
            ingredients = []
            for _ in range(count_ingredients):
                ingredient_line = f.readline().strip()
                ingredient_info = ingredient_line.split(' | ')
                name = ingredient_info[0]
                quantity = int(ingredient_info[1])
                measure = ingredient_info[2]
                ingredient_info = {'ingredient_name': name, 'quantity': quantity, 'measure': measure}
                ingredients.append(ingredient_info)
            recipe[dish] = ingredients
            f.readline()
            line = f.readline().strip()
    return recipe


print(read_recipes())

dishes = list(input('Введите через запятую названия блюд, которые хотите приготовить: ').split(', '))
person_count = int(input('Укажите количество людей: '))


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = read_recipes()
    buy_products = {}

    for dish in dishes:
        ingredients = cook_book[dish]
        for ingredient in ingredients:
            quantity = ingredient['quantity'] * person_count
            name = ingredient['ingredient_name']
            if name in buy_products:
                buy_products[name]['quantity'] += quantity
            else:
                buy_products[name] = {'measure': ingredient['measure'], 'quantity': quantity}

    print(buy_products)


get_shop_list_by_dishes(dishes, person_count)