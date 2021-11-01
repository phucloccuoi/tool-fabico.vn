from re import compile, sub

# Hàm chia nhỏ chuỗi lớn thành các chuỗi con
def split_big_str(input_string, str_slit, num_sub_str, remove_newline):
    '''
    Function: chia nhỏ chuỗi lớn thành các chuỗi con và cho vào dánh sách
    - input_string: Chuỗi đầu vào cần được chia nhỏ
    - str_slit: Chuỗi phân cách giữa các chuỗi con
    - num_sub_str: Số thứ tự
    - remove_newline: Nếu =1 thì sẽ xóa ký tự xuống dòng cuỗi dòng
    Return: Danh sách các chuỗi con
    '''
    # Tách các chuỗi thành chuỗi con khi gặp chuỗi nhận dạng thành num_sub_str
    list_sub_string = input_string.split(str_slit, num_sub_str)

    # Xóa ký tự xuống dòng trong string
    if remove_newline == 1:
        temp = list_sub_string[num_sub_str]
        temp = temp.rstrip("\n")
        list_sub_string[num_sub_str] = temp

    return str(list_sub_string)
# Kết thúc hàm chia nhỏ chuỗi lớn thành các chuỗi con

# Hàm thay thế các chuỗi thẻ html
def repalce_str_html(old_str, change_str, changed_str):
    '''
    Function: xóa các chuỗi thẻ html không cần thiết
    - old_str: Chuỗi cần thay thế
    - find_str: Chuỗi cần thay thế
    - changed_str: Chuỗi sẽ thay thế
    Return: Ký tự khoảng trống cho chuỗi đầu vào
    '''
    # Tìm các thẻ <>
    cleanr = compile(change_str)

    # Xóa các thẻ <> chỉ chừa lại text
    cleantext = sub(cleanr, changed_str, old_str)

    return cleantext
# Kết thúc hàm thay thế các chuỗi thẻ html

# Hàm xóa chuỗi thừa
def delete_str_unnecessary(str_deleted, list_str_del):
    '''
    Function: Xóa các thuộc tính, thẻ không cần thiết
    - str_deleted: Chuỗi cần xử lý
    - list_str_del: Danh sách những chuỗi sẽ xóa
    Return: Chuỗi khi đã xóa
    '''
    # Khai báo biến chuỗi tạm thời & số chuỗi cần xóa
    temp_string = ''
    numFind_black = len(list_str_del)

    # Xóa các ký tự không cần thiết trong black_list
    for numfind in range(0, numFind_black):
        temp_string = str(str_deleted)
        str_deleted = ''
        str_deleted = repalce_str_html(temp_string, list_str_del[numfind], '')
    
    return str_deleted
# Kết quả hàm xóa chuỗi thừa

# Hàm thêm chuỗi từ danh sách
def add_str_description(str_added, list_str_change, list_str_changed):
    '''
    Function: Thêm và chỉnh sửa các thuộc tính của chuỗi HTML
    - str_added: Chuỗi cần xử lý
    - list_str_change: Danh sách chuỗi cần thay đổi
    - list_str_changed: Danh sách chuỗi sẽ thay đổi
    Return: Chuỗi khi đã thêm các thuộc tính
    '''
    # Khai báo biến chuỗi tạm thời & số chuỗi cần thêm
    temp_string = ''
    numFind_change = len(list_str_change)
    
    # Thay đổi các ký tự trong change_list thành changed_list
    for numfind in range(0, numFind_change):
        temp_string = str(str_added)
        str_added = ''
        str_added = repalce_str_html(temp_string, list_str_change[numfind], list_str_changed[numfind])

    return str_added
# Kết quả hàm thêm chuỗi từ danh sách

# Hàm chỉnh sửa mô tả theo định dạng người dùng
def format_description(list_desc_full, name_product):
    '''
    Function: Định dạng lại các thẻ trong html như mong muốn
    - html_string: Chuỗi cần xử lý và trả về chuỗi đã định dạng
    - name_product: Tên sản phẩm
    Return: Chuỗi có dịnh dạng ngon lành
    '''
    # Danh sách các chuỗi sẽ xóa
    black_list = ['\sclass="[a-z _-]+?"', '<(\/)?col.*?>', '<(\/)?div.*>', 'style=".*?"', '\t']

    # Danh sách các chuỗi sẽ thay đổi
    change_list = ['href="+(.*)?"', '<th>', '\n', '<table>']
    changed_list = ['style="font-size: 14px; color: #ff5050;" href="https://www.fabico.vn/"', '<th style="text-align: left;">', ' ', '<table style="width:570px">']

    # Gọi các hàm thêm xóa mô tả table
    str_desc_0 = str(delete_str_unnecessary(list_desc_full[0], black_list))
    str_desc_0 = str(add_str_description(str_desc_0, change_list, changed_list))

    # Gọi các hàm thêm xóa mô tả paragraph
    str_desc_1 = str(delete_str_unnecessary(list_desc_full[1], black_list))
    str_desc_1 = str(add_str_description(str_desc_1, change_list, changed_list))

    # Định dạng heading cho tên sản phẩm
    name_h2 = "<h2><strong>" + name_product + "</strong></h2>\n"
    name_h3 = "<h3><strong>" + name_product + "</strong></h3>\n"

    # Thêm định dạng các thẻ tên cho chuỗi table
    str_desc_0 = str(name_h2 + "<div>" + str_desc_0 + "</div>")
    
    # Nếu có chuỗi tên thì thôi bó tay ### ERRORRRRRRRRRRRRRRRRRRRRRRRR
    if str_desc_1.find(name_product) != -1:
        str_desc_1.replace(name_product, '', 2)
    else:
        # Thêm định dạng các thẻ tên cho chuỗi paragraps
        str_desc_1 = str(name_h3 + str_desc_1)

    return str_desc_0 + "<hr/>" + str_desc_1
# Kết thúc hàm chỉnh sửa mô tả theo định dạng người dùng

# Hàm định dạng mô tả cho trường SEO
def get_description_SEO(desc_SEO):
    '''
    Function: Định dạng lại phần mô tả SEO
    - desc_SEO: chuỗi cần xử lý và trả về chuỗi đã định dạng
    Return: chuỗi có dịnh dạng ngon lành
    '''
    # Gọi hàm xóa các tag
    desc_SEO = repalce_str_html(desc_SEO, '<.*?>', '')

    # Danh sách các từ khóa cần chuyển đổi
    letters_Markups = ['&Agrave;', '&Egrave;', '&Igrave;', '&Ograve;', '&Ugrave;', '&agrave;', '&egrave;', '&igrave;', '&ograve;', '&ugrave;',
    '&Aacute;', '&Eacute;', '&Iacute;', '&Oacute;', '&Uacute;', '&Yacute;', '&aacute;', '&eacute;', '&iacute;', '&oacute;', '&uacute;', '&yacute;',
    '&Acirc;', '&Ecirc;', '&Ocirc;', '&acirc;', '&ecirc;', '&ocirc;', '&Atilde;', '&Otilde;', '&atilde;', '&otilde;', '&nbsp;']
    # Danh sách các từ khóa sẽ thay thế
    letters_Accents = ['À', 'È', 'Ì', 'Ò', 'Ù', 'à', 'è', 'ì', 'ò', 'ù',
    'Á', 'É', 'Í', 'Ó', 'Ú', 'Ý', 'á', 'é', 'í', 'ó', 'ú', 'ý',
    'Â', 'Ê', 'Ô', 'â', 'ê', 'ô', 'Ã', 'Õ', 'ã', 'õ', ' ']

    # Chỉnh sửa các ký tự đặc biệt thành ký tự có dấu
    desc_SEO = str(add_str_description(desc_SEO, letters_Markups, letters_Accents))
    desc_SEO = " ".join(desc_SEO.split())

    # Biến lưu trữ vị trí tối đa chuỗi SEO
    saveIndex = 0
    endStr = 320

    # Kiểm tra độ dài của chuỗi xem có nhỏ hơn 320 không
    lengtStr = len(desc_SEO)
    if lengtStr <= 320:
        endStr = lengtStr

    # Giới hạn độ dài của chuỗi SEO chỉ được tối đa 320 ký tự
    for index in range(0, endStr):
        if desc_SEO[index] == '.':
            saveIndex = index
    
    # Lấy chuỗi SEO chuẩn dưới 320 ký tự
    if saveIndex == 0:
        desc_SEO = desc_SEO[0:endStr]
    else:
        desc_SEO = desc_SEO[0:saveIndex]

    return desc_SEO
# Kết thúc hàm định dạng mô tả cho trường SEO