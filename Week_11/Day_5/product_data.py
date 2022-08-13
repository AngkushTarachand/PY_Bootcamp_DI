import json


def retrieve_all_products():
    json_file = 'products.json'
    with open(json_file, 'r') as file_obj:
        all_product = json.load(file_obj)

    return all_product


def retrieve_requested_product(product_id):
    json_file = 'products.json'
    with open(json_file, 'r') as file_obj:
        data = json.load(file_obj)
    for each in data:
        if each['ProductId'] == product_id:
            print(each['ProductId'])
