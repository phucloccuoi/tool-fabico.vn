# Modules
import requests
from time import sleep

# Get products_id function
def get_products_id(listBarcode, headerToken):
    '''
    Function: Lấy products_id trên fabico và lưu vào danh sách
    Return: Danh sách sản phẩm
    '''

    print('--GET PRODUCTS ID--')

    listProd_ID = []
    count = 1
    headerFabico = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {headerToken}'
    }

    # Tìm kiếm từng sản phẩm
    for barcode in listBarcode:
        # Truy cập vào trang tìm kiếm sản phẩm
        try:
            respone = requests.get(url=f'https://www.fabico.vn/search?type=product&q={barcode}', headers=headerFabico)
        except AttributeError:
            return -1

        payload = respone.text

        # Nếu sản phẩm đã bị ẩn thì không cẩn lưu vào danh sách
        if payload.find("countdown_") == -1:
            count += 1
            continue

        # Tách chuỗi làm đôi
        payload = payload.split('countdown_')

        # Lấy 10 ký tự đầu tiên của phần tử thứ 2 và lưu vào danh sách
        listProd_ID.append((payload[1])[0:10] + '\n')

        print('_Get_Product_ID', count)
        sleep(1)
        count += 1

    return listProd_ID
# end get products_id

# update products function
def update_Prod(listProd_ID, headerToken):

    print('--UPDATE PRODUCTS--')

    with open('data_update.json', 'r') as file_data:
        data_update = file_data.read()

    count = 1

    headerFabico = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {headerToken}'
    }

    # Hide all products in the list
    for product_id in listProd_ID:
        respone = requests.put(url=f'https://apis.haravan.com/com/products/{product_id}.json', data=data_update, headers=headerFabico)

        # Conplte a product
        print('_Update product', count)
        count += 1
        sleep(1)
    
    if respone.status_code == 200:
        return 1
    else:
        return -1
# end update products

# delete products function
def delete_Prod(listProd_ID, headerToken):

    print('--DELETE PRODUCTS--')

    count = 1
    headerFabico = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {headerToken}'
    }

    # Hide all products in the list
    for product_id in listProd_ID:
        respone = requests.delete(url=f'https://apis.haravan.com/com/products/{product_id}.json', data='{\}', headers=headerFabico)

        # Conplte a product
        print('_Delete product', count)
        count += 1
        sleep(1)
    
    if respone.status_code == 200:
        return 1
    else:
        return -1
# end delete products

# Hàm kiểm tra sản phẩm có trên website hay không
def check_products_duplication(listBarcode, headerToken):

    listProd_Duplication = []
    count = 1
    headerFabico = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {headerToken}'
    }

    # Tìm kiếm từng sản phẩm
    for barcode in listBarcode:
        # Truy cập vào trang tìm kiếm sản phẩm
        try:
            respone = requests.get(url=f'https://www.fabico.vn/search?type=product&q={barcode}', headers=headerFabico)
        except AttributeError:
            return -1

        payload = respone.text

        # Tách chuỗi làm đôi
        payload = payload.split('collection-size')

        # Lấy ký tự chứa số lượng sản phẩm trên website
        result =  payload[1][3:4]

        
        if result == '0':
            print(f"_Product {count} is hiding!")
        elif result != '1':
            listProd_Duplication.append(barcode)
            print('_There are ' + result + ' products')
        else:
            print(f"_Product {count} not duplicated!")
        sleep(1)
        count += 1

    return listProd_Duplication
# Kết thúc hàm kiểm tra sản phẩm trên website