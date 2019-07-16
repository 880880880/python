import json

def write_order_to_json(item_arg, quantity_arg, price_arg, buyer_arg, date_arg):
    with open('orders.json','r+') as file: # читаем текущие заказы
        dict_in=json.load(file)
        dict_in["orders"].append({'item':item_arg, 'quantity':quantity_arg, 'price':price_arg, 'buyer':buyer_arg, 'date':date_arg}) # добавляем новый
    with open('orders.json','w') as file:
         json.dump(dict_in, file, indent=4) # пишем в файл
    return 1

write_order_to_json(1,1,1,1,1)
write_order_to_json(2,2,2,2,2)
write_order_to_json(3,3,3,3,3)
write_order_to_json('sij', 'wfwf', 'fwf', 'wegre', 4)


# {
#     "orders": [
#         {
#             "item": 1,
#             "quantity": 1,
#             "price": 1,
#             "buyer": 1,
#             "date": 1
#         },
#         {
#             "item": 2,
#             "quantity": 2,
#             "price": 2,
#             "buyer": 2,
#             "date": 2
#         },
#         {
#             "item": 3,
#             "quantity": 3,
#             "price": 3,
#             "buyer": 3,
#             "date": 3
#         },
#         {
#             "item": "sij",
#             "quantity": "wfwf",
#             "price": "fwf",
#             "buyer": "wegre",
#             "date": 4
#         }
#     ]
#  }