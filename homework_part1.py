import pprint
cook_book = {}

with open('recipes.txt') as f:
        lines = f.readlines()
        i = 0
        while i < len(lines):
            dish_name = lines[i].strip()
            i += 1
            ingredient_count = int(lines[i].strip())
            i += 1
            ingredients = []
            for j in range(ingredient_count):
                ingredient_info = lines[i].strip().split(' | ')
                ingredient_name = ingredient_info[0]
                quantity = int(ingredient_info[1])
                measure = ingredient_info[2]
                ingredient_dict = {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure}
                ingredients.append(ingredient_dict)
                i += 1
            cook_book[dish_name] = ingredients
            i += 1

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            ingredients = cook_book[dish]
            for ingredient in ingredients:
                name = ingredient['ingredient_name']
                measure = ingredient['measure']
                quantity = ingredient['quantity'] * person_count
                if name in shop_list:
                    shop_list[name]['quantity'] += quantity
                else:
                    shop_list[name] = {'measure': measure, 'quantity': quantity}
    return shop_list

pprint.pp(cook_book)
pprint.pp(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))