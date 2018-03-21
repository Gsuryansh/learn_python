import xlrd

def pasre_user_information():
    workbook = xlrd.open_workbook("userinformation.xlsx")
    sheet = workbook.sheet_by_name("credential")
    user_information = []
    header = []

    for row in range(sheet.nrows):
            if sheet.row_values(row)[0] == "USERNAME":
                continue
            else:
                user_information[sheet.row_values(row)[0]] = sheet.row_values(row)[1]
    print(user_information)
pasre_user_information()

