from requests_html import HTMLSession, HTML
from pyppeteer import errors
from time import sleep

list_all_links_product = [] # Danh sách các link sản phẩm
list_all_html_products = [] # Danh sách các respone trả về

# Hàm tạo một phiên kết nối vào một website với liên kêt cho trước
def get_session(url_full, time_out):
    '''
    - Chức năng: tạo một phiên kết nối vào một website với liên kêt cho trước
    - url_full: địa chỉ website muốn truy cập
    - time_out: Thời gian phản hồi của website, sau đó sẽ đóng
    - result_page: hàm trả về biến loại HTML lưu toàn bộ thông tin html của website
    '''
    # Khởi tạo một phiên kết nối
    my_session = HTMLSession()

    try:
        # Tạo một phiên kết nối tới trang đích
        my_response = my_session.get(url_full)

        # Tổng thời gian Loading bằng thời gian tối đa là 6s + 2s và tối thiểu là 2s + 2s
        try:
            my_response.html.render(scrolldown=1, sleep=time_out, keep_page=True)
        except ConnectionRefusedError:
            my_response.html.render(scrolldown=1, sleep=time_out + 1, keep_page=True)
        except RuntimeError:
            my_response.html.render(scrolldown=1, sleep=time_out + 2, keep_page=True)
        except errors.NetworkError:
            my_response.html.render(scrolldown=1, sleep=time_out - 1, keep_page=True)
        finally:
            my_session.close()
    except errors.TimeoutError:
        sleep(time_out/2)
        my_response.html.render(scrolldown=1, sleep=time_out, keep_page=True)
    finally:
        my_session.close()

    # Lưu kết quả trả về với định dạng theo kiểu HTML
    result_page = HTML(html = my_response.html.html)

    return result_page
# Kết thúc hàm tạo một phiên kết nối vào một website với liên kêt cho trước

# Hàm lấy link sản phẩm từ trang tìm kiếm
def get_link_product(barcode):
    '''
    - Chức năng: lấy ra chính xác link sản phẩm 
    - Hàm trả về 1: nếu thêm thành công link sản phẩm vào danh sách
    - Hàm trả về -1: nếu sản phẩm không có trên trang fahasa, vẫn lưu vào danh sách respone rỗng
    - ordinal_number_product: số thứ tự của sản phẩm trong file thông tin
    '''
    # Truy cập tới trang tìm kiếm sản phẩm
    search_page = get_session(f"https://www.fahasa.com/search?in_stock=0&q={barcode}", 6)

    try:
        # Tìm kiếm tới thẻ có chứa link sản phẩm
        find_link = search_page.find("div.item-inner", first=True)
        link_product = find_link.find("a.product-image", first=True)
    except AttributeError:
        # Nếu không tìm thấy sản phẩm thì lưu vào danh sách chuỗi rỗng
        list_all_links_product.append('')
        list_all_html_products.append('')
        return -1

    # Thêm chuỗi chứa link sản phẩm vào dánh sách
    list_all_links_product.append(str(link_product.attrs["href"]))

    return 1
# Kết thúc hàm lấy link sản phẩm từ trang tìm kiếm

# Hàm truy cập vào trang sản phẩm
def access_product_page(ordinal_number_product):
    '''
    - Chức năng: Truy cập vào trang sản phẩm 
    - ordinal_number_product: số thứ tự của sản phẩm trong file thông tin
    - product_page: Hàm trả về giá trị có kiêu HTML của trang đích
    '''
    # Lấy url sản phẩm từ danh sách
    url_product = list_all_links_product[ordinal_number_product]
    
    # Truy cập tới trang sản phẩm
    product_page = get_session(url_product, 6)

    # Thêm respone sản phẩm vào danh sách lưu trữ respone
    list_all_html_products.append(product_page)

    # Vẫn phải trả về kết quả do luồng truy cập đầu tiên từ hàm khác
    return product_page
# Kết thúc hàm truy cập vào trang sản phẩm