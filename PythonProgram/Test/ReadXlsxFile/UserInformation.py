""" It will read the file and get the name of all the sheet present in the file """

import xlrd
import sys
from ReadXlsxFile import GetFileName
from ReadXlsxFile.ShowInHtml import ShowHtml

class ReadUserInformation(object):

    def __init__(self,file_name):
        self.file_name = file_name

    def open_file(self):
        return xlrd.open_workbook(self.file_name)
    #return a list of all the file name
    def number_of_users(self,file):
        return file.sheet_names()

    def convert_html(self,user_info):
        obj = ShowHtml(self.file_name,user_info)
        obj.show_html()

if __name__ == "__main__":
    name = GetFileName.get_file_name()

    if name == None:#Checking if the file is present or not
        print("No such file exist")
        sys.exit(1)
    user = ReadUserInformation(name)
    workbook = user.open_file()
    sheet_names = user.number_of_users(workbook)
    #for each file it will call the conver html method and creat html for each sheet
    for value in sheet_names:
        user.convert_html(value)






