# Khai báo các modules cần sử dụng
from datetime import datetime
import csv
import handing_string
import request_page

# Hàm lấy ra tên sản phẩm
def get_name_product(indexList):
    '''
    - Chức năng: lấy ra tên sản phẩm
    - name_product: trả về tên sản phẩm cần tìm
    - indexList: số thứ tự của sản phẩm trong file thông tin sản phẩm
    '''
    source_page = request_page.access_product_page(indexList)
    name_product = ''

    try:
    # Tìm kiếm tên
        temp = source_page.find("a.include-in-gallery", first=True)
        name_product = temp.attrs["title"]
    except AttributeError:
        return -1
    finally:
        return str(name_product).strip()
# Kêt thúc hàm lấy ra tên sản phẩm

# Hàm lấy thông tin Url theo đinh dạng "viet-chi-staedtler-134-2b"
def get_link_to_format(indexList):
    '''
    - Chức năng: Lấy chuỗi theo định dạng cuỗi link Ex:viet-chi-staedtler-134-2b
    - indexList: số thứ tự của sản phẩm trong file thông tin
    - url_short: Hàm trả về giá trị có kiểu chuỗi có đinh dạng cho theo yêu cầu
    '''
    url_product = request_page.list_all_links_product[indexList]

    # Chuyển sang chuỗi
    url_short = str(url_product)

    return str(url_short[23:-5])
# Kết thúc lấy thông tin Url theo đinh dạng "viet-chi-staedtler-134-2b"

# Hàm lấy Link hình của sản phẩm
def get_all_links_images_product(indexList):
    '''
    - Chức năng: Lấy tất cả các link hình ảnh của sản phẩm và lưu vào danh sách
    - list_links_images: Trả về danh sách các link của sản phẩm
    - indexList: số thứ tự của sản phẩm trong file thông tin
    '''
    # Truy cập vào trang sản phẩm
    source_page = request_page.list_all_html_products[indexList]

    # Tìm kiếm các link hình trong trang sản phẩm
    find_element1 = source_page.find("div.swiper-wrapper", first=True)
    find_element2 = find_element1.find("img.swiper-lazy")
    
    # Tạo danh sách lưu các link
    list_links_images = []

    # Gán các link tìm được vào danh sách
    for number_links in range(0, len(find_element2)):
        list_links_images.append(find_element2[number_links].attrs["src"])
    
    # Trả về danh sách các link của sản phẩm
    return list_links_images
# Kết thúc hàm lấy Link hình của sản phẩm

# Hàm lấy mô tả của sản phẩm và định dạng theo chuẩn
def get_description(indexList):
    '''
    - Chức năng: lấy các giá trị mô tả trong phần mô tả sản phẩm
    - string_description_product: trả về chuỗi thu về từ trang đích
    - indexList: số thứ tự của sản phẩm trong file thông tin
    - name_product: lấy tên sản phẩm cho vào phần mô tả
    '''
    # Truy cập vào trang sản phẩm
    source_page = request_page.list_all_html_products[indexList]

    # Tìm kiếm các mô tả
    description_product = source_page.find("div.std", first=True)
    description_product_table = source_page.find("div.product_view_tab_content_additional", first=True)

    try:
        list_desc_full = [ description_product_table.html, description_product.html]
    except AttributeError:
        return -1

    return list_desc_full
# Kết thúc hàm lấy mô tả của sản phẩm và định dạng theo chuẩn

# Hàm lấy thời gian hiện tại
def get_time_now():
    '''
    - Chức năng: lấy thời gian tại thời điểm hiện tại theo định dạng
    - formatTime: trả về chuỗi time theo định dạng Ngày/Tháng/Năm Giờ:Phút:Giây
    '''
    # Lấy thời gian hiện tại
    timeNow = datetime.now()

    # Định dạng thời gian
    formatTime = timeNow.strftime("%d/%m/%Y %H:%M:%S")

    return formatTime
# Kêt thúc hàm lấy thời gian hiện tại

# Hàm ghi các tiêu đề vào file output.csv
def write_header_to_file(fileName):
    '''
    - Chức năng: ghi tiêu đề vào file
    - Trả về 1: nếu việc ghi hoàn tất
    '''
    with open(fileName, 'w', newline = '', encoding='utf-8') as file_output:
            # Khai báo danh sách các tiêu đề
            headers = ['Url', 'Tên', 'Mô tả', 'Trích dẫn', 'Hãng', 'Loại sản phẩm', 'Tag', 'Hiển thị', 
                        'Thuộc tính 1', 'Giá trị thuộc tính 1', 'Thuộc tính 2', 'Giá trị thuộc tính 2', 
                        'Thuộc tính 3', 'Giá trị thuộc tính 3', 'Mã phiên bản sản phẩm', 'Khối lượng', 
                        'Quản lý tồn kho', 'Số lượng tồn kho', 'Đặt hàng khi hết hàng', 'Variant Fulfillment Service', 
                        'Giá', 'Giá so sánh', 'Có giao hàng không?', 'Variant Taxable', 'Barcode', 'Link hình', 
                        'Mô tả hình', 'Gift Card', 'SEO Title', 'SEO Description', 'Google Shopping / Google Product Category', 
                        'Google Shopping / Gender', 'Google Shopping / Age Group', 'Google Shopping / MPN', 
                        'Google Shopping / AdWords Grouping', 'Google Shopping / AdWords Labels', 'Google Shopping / Condition', 
                        'Google Shopping / Custom Product', 'Danh mục', 'Danh mục EN', 'Ảnh biến thể', 'Ngày tạo', 'Ngày cập nhật', 
                        'Hiển thị kênh bán hàng Lazada', 'Hiển thị kênh bán hàng Zalo', 'Hiển thị kênh bán hàng Zalora', 
                        'Hiển thị kênh bán hàng Sendo', 'Hiển thị kênh bán hàng Adayroi', 'Hiển thị kênh bán hàng FacebookShop', 
                        'Hiển thị kênh bán hàng Tiki', 'Hiển thị kênh bán hàng Google', 'Hiển thị kênh bán hàng Shopee', 
                        'Không áp dụng khuyến mãi', 'Hiển thị kênh bán hàng HaraRetail']
            
            # ghi các tiêu đề vào file
            writer = csv.writer(file_output, delimiter=',')
            writer.writerow(headers)

    file_output.close()
    return 1
# Kêt thúc hàm ghi các tiêu đề vào file output.csv

# Hàm ghi barcode lỗi vào file
def write_log(barcode):
    # Nếu sản phẩm không có trên website hoặc lỗi thì lưu vào file
    with open('Data\\error_products.log', 'a+', encoding='utf-8') as error:
        error.writelines(barcode + '\n')
    error.close()
# Kết thúc ghi barcode lỗi vào file

# Hàm ghi các giá trị thu thập được vào file
def write_info_to_file(strProdInList, fileName, indexList):
    '''
    - Chức năng: ghi thông tin thu thập được vào file
    - Trả về 1: nếu việc ghi hoàn tất
    - Trả về -1: nếu không có sản phẩm trên fahasa, và lưu barcode lỗi vào error_products.log
    '''
    #----------------------------Khu vực kiểm tra các biến gán đầu vào-----------------------##
    # Giá trị cho cột Barcode
    barcode = handing_string.split_big_str(strProdInList, ",", 4, 1)[0]
    result_page_product = request_page.get_link_product(barcode)

    if result_page_product == -1:
        print('>>> No products found!')
        write_log(barcode)
        return -1
    else:
    # Giá trị cột Url
        urlShort = get_link_to_format(indexList)

        # Giá trị cho cột Tên sản phẩm
        nameProduct = get_name_product(indexList)
        if (nameProduct == -1):
            return -1

        # Giá trị cho cột tồn kho
        inventory = handing_string.split_big_str(strProdInList, ",", 4, 1)[4]

        # Giá trị cho cột Mô tả
        list_str = get_description(indexList)
        # Kiểm tra xem có mô tả hay không, nếu không có thì ghi vào file lỗi
        if list_str == -1:
            print('>>> No products found!')
            write_log(barcode)
            return -1
        desc_full = handing_string.format_description(list_str, nameProduct)

        # Giá trị cho cột Mô tả SEO
        desc_320_char = handing_string.get_description_SEO(list_str[1])
        
        # Giá trị cho cột Nhà cung cấp
        valueProducer = handing_string.split_big_str(strProdInList, ",", 4, 1)[3]

        # Giá trị cho cột loại sản phẩm
        type_product = handing_string.split_big_str(strProdInList, ",", 4, 1)[2]

        # Giá trị cho cột Link hình
        list_link_images = get_all_links_images_product(indexList)

        # Giá trị cho cột Ngày hiện tại và cột ngày cập nhập
        timeNow = get_time_now()

        # Khai báo số lượng sản phẩm và số hàng của từng sản phẩm
        number_imgages = len(get_all_links_images_product(indexList))

        # Giá trị cột giá của sản phẩm
        price_product = handing_string.split_big_str(strProdInList, ",", 4, 1)[1]
    #------------------------Kết thúc khu vực kiểm tra các biến gán đầu vào-----------------------##

        # Mở file output.csv và ghi các giá trị thu thập vào file
        with open(fileName, 'a+', newline = '', encoding='utf-8') as file_output:
            # Khai báo đối tượng ghi file
            writer = csv.writer(file_output, delimiter=',')

            # Cho vòng lặp chạy tạo mỗi hình là một hàng
            for numberImages in range(0, number_imgages):
                if numberImages == 10:
                    break
                value_row = [urlShort, nameProduct, desc_full, 
                                    '', valueProducer, type_product, type_product, 'Yes', 
                                    'Title', 'Default Title', '', '', '', '', barcode, '0', 'Haravan', 
                                    inventory, 'deny', '', price_product, price_product, 'Yes', 
                                    'Yes', barcode, list_link_images[numberImages], nameProduct, 
                                    'No', nameProduct, desc_320_char, '', '', '', '', '', '', '', '', '', 
                                    '', '', timeNow, timeNow, 'No', 'No', 'No', 'No', 'No', 'No', 'No', 
                                    'Yes', 'No', 'No', 'Yes']
                value_row_image = [urlShort, '', '', '', '', '', '', 'Yes', '', '', '', '', '', '', 
                                    '', '', '', '0', 'deny', '', '', '', 'No', 'No', '', 
                                    list_link_images[numberImages], nameProduct, 'No', '', '', '', 
                                    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 
                                    '', '', '', '', 'No', 'No']
                if numberImages == 0:
                    writer.writerow(value_row)
                elif numberImages > 0:
                    writer.writerow(value_row_image)
        file_output.close()
        print(f"- Finish product {indexList}")
    return 1
# Kết thúc hàm xóa ghi các giá trị thu thập được vào file