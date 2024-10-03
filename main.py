cook_book = {}
with open('recipies.txt', 'rt', encoding='utf-8') as file:
    dishes = ''
    for dish in file:
        dish = dish.strip()
        if dish.isdigit():
            continue
        elif dish and '|' not in dish:
            cook_book[dish] = []
            dishes = dish
        elif dish and '|' in dish:
            a, b, c = dish.split(" | ")
            cook_book.get(dishes).append(dict(ingredient_name=a, quantity=int(b), measure=c))

print(cook_book)

def get_shop_list_by_dishes(dishes_list, person_count):
    shop_list = {}
    for dish in dishes_list:
        if dish in cook_book:
            for ingredients in cook_book[dish]:
                if ingredients['ingredient_name'] in shop_list:
                    shop_list[ingredients['ingredient_name']]['quantity'] += ingredients['quantity'] * person_count
                else:
                    shop_list[ingredients['ingredient_name']] = ({'measure': ingredients['measure'], 'quantity':
                                                                (ingredients['quantity'] * person_count)})
        else:
            print('Такого блюда нет в меню')
    return shop_list
print(get_shop_list_by_dishes(['Омлет'], 2))



