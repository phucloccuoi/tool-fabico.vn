# import modules
from os import system, name, path
import fahasa_crawler
import handing_file
import call_api_fabico

# Clear function
def clear():

	# for windows
	if name == 'nt':
		_ = system('cls')

	# for mac and linux(here, os.name is 'posix')
	else:
		_ = system('clear')
# end clear function

# Menu function
def main_Menu():

    # call function clear screen
    clear()

    # Introdution
    print(",------. ,---.  ,-----.  ,--. ,-----. ,-----.     ,--.   ,--.,------.,-----.   ,---.  ,--.,--------.,------.    ,--------. ,-----.  ,-----. ,--.       ")
    print("|  .---'/  O  \ |  |) /_ |  |'  .--./'  .-.  '    |  |   |  ||  .---'|  |) /_ '   .-' |  |'--.  .--'|  .---'    '--.  .--''  .-.  ''  .-.  '|  |       ")
    print("|  `--,|  .-.  ||  .-.  \|  ||  |    |  | |  |    |  |.'.|  ||  `--, |  .-.  \`.  `-. |  |   |  |   |  `--,        |  |   |  | |  ||  | |  ||  |       ")
    print("|  |`  |  | |  ||  '--' /|  |'  '--' \'  '-'  '    |   ,'.   ||  `---.|  '--' /.-'    ||  |   |  |   |  `---.       |  |   '  '-'  ''  '-'  '|  '--.    ")
    print("`--'   `--' `--'`------' `--' `-----' `-----'     '--'   '--'`------'`------' `-----' `--'   `--'   `------'       `--'    `-----'  `-----' `-----'    ")
    print("\t\t\t\t\t\t\tWriter by Nguyen Phuoc Loc!!!")

    # Main menu
    print("\n-------------------------------")
    print("| 0. Exit.                    |")
    print("| 1. Crawlling Data Fahasa.   |")
    print("| 2. Check Product Dulicates. |")
    print("| 3. Update Product From File.|")
    print("| 4. Delete Product.          |")
    print("-------------------------------")

    return 1
# end main menu

# crawler fahasa function
def crawler():
    listBarcodeCrawler_InFileName = input('\\_Please enter file name of barcode input list name want to get data> ')
    listBarcodeCrawler_OutFileName = input('\\_Please enter file name of barcode output list name want to get data> ')

    # 
    while path.isfile("Data\\" + listBarcodeCrawler_InFileName + ".txt") != 1:
        print('\\_There is no file you requested!!!')
        listBarcodeCrawler_InFileName = input('\\_Please RE-ENTER the barcode input name of the list you want to get data> ')
        
    listProduct = handing_file.read_file_to_list(("Data\\" + listBarcodeCrawler_InFileName + ".txt"))

    # Khởi tạo biến bắt đầu vòng lặp
    indexList = 0

    fahasa_crawler.write_header_to_file("Data\\" + listBarcodeCrawler_OutFileName + ".csv")

    for Prod in listProduct:
        fahasa_crawler.write_info_to_file(Prod, "Data\\" + listBarcodeCrawler_OutFileName + ".csv", indexList)
        indexList += 1

    return 1
# end crawler fahasa

# check duplication function
def check_Duplication():

    secretToken = input('\\_Please enter the secret token haravan> ')
    checkDup_FileName = input('\\_Please enter barcode input list name want to check> ')
    noneDup_FileName = input('\\_Please enterbarcode output list name want to check> ')

    while path.isfile("Data\\" + checkDup_FileName + ".txt") != 1:
        print('\\_There is no file you requested!!!')
        checkDup_FileName = input('\\_Please PRE-ENTER barcode input list name want to check> ')

    # Khai báo danh sách barcode đầu vào
    list_barcode_first_filter = handing_file.read_file_to_list("Data\\" + checkDup_FileName + ".txt")
    print('--CHECK IN STARTS FABICO--')

    # Gọi hàm kiểm tra sản phẩm fabico và ghi vào file
    list_not_Found_Fabico = call_api_fabico.check_products_duplication(list_barcode_first_filter, secretToken)
    handing_file.write_list_to_file(list_not_Found_Fabico, len(list_not_Found_Fabico), "Data\\" + noneDup_FileName + ".txt")
    

    print("-------FINISH--------")
    return 1
# end check duplication

# update products function
def update_Products():
    secretToken = input('\\_Please enter the secret token haravan> ')
    listBarcodeUpdate_InFileName = input('\\_Please enter file name of barcode intput list name want to update>')

    while path.isfile("Data\\" + listBarcodeUpdate_InFileName + ".txt") != 1:
        print('\\_There is no file you requested!!!')
        listBarcodeUpdate_InFileName = input('\\_Please PRE-ENTER barcode input list name want to update> ')

    listProd_BarCode = handing_file.read_file_to_list("Data\\" + listBarcodeUpdate_InFileName + ".txt")

    listProd_ID = call_api_fabico.get_products_id(listProd_BarCode, secretToken)

    if listProd_ID == -1:
        update_Products()

    return call_api_fabico.update_Prod(listProd_ID, secretToken)
# end update 

# delete products function
def delete_Products():
    secretToken = input('\\_Please enter the secret token haravan> ')
    listBarcodeDelete_InFileName = input('\\_Please enter file name of barcode intput list name want to delete>')

    while path.isfile("Data\\" + listBarcodeDelete_InFileName + ".txt") != 1:
        print('\\_There is no file you requested!!!')
        listBarcodeDelete_InFileName = input('\\_Please PRE-ENTER barcode input list name want to update> ')

    listProd_BarCode = handing_file.read_file_to_list("Data\\" + listBarcodeDelete_InFileName + ".txt")

    listProd_ID = call_api_fabico.get_products_id(listProd_BarCode, secretToken)

    if listProd_ID == -1:
        delete_Products()

    return call_api_fabico.delete_Prod(listProd_ID, secretToken)
# end delete products

# Directional function
def router(user_input):
    if user_input == 0:
        print('BYE!!!')
    elif user_input == 1:
        crawler()
    elif user_input == 2:
        check_Duplication()
    elif user_input == 3:
        update_Products()
    elif user_input == 4:
        delete_Products()
    return 1
# end directoinal

# ------------------------------------ROOT----------------------------------- #
if __name__ == '__main__':
    
    # Variables
    continue_program = 'y' # Default is 6

    while continue_program == 'y':

        # Main menu
        main_Menu()

        # Input user
        user_input = int(input('Please choose the number of the job you want to do> '))

        # Router
        router(user_input)

        # Ask the user what else they want to do
        continue_program = input('What else do you want to do(y/n))? ')
