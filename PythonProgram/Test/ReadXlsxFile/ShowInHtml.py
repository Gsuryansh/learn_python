import  pandas as pd

""" Class ShowHtml will  read the Xlsx file and creat html report for every sheet in the xlsx file """

class ShowHtml(object):

    def __init__(self,file_name,sheet_name):#It will take two argument xlsx file name and sheet name
        self.file_name = file_name
        self.sheet_name = sheet_name

    def show_html(self):#Will creat html file from xlsx file
        rd = self.read_excel()
        parse_file = self.parse_excel(rd)
        self.convert_html(parse_file)
    #Read The xlsx file
    def read_excel(self):
        return pd.ExcelFile(self.file_name)
    #parse The xlsx file
    def parse_excel(self,file):
        return file.parse(self.sheet_name)

    #Creat html file from xlsx file with file name as sheet name
    def convert_html(self,file):
        html_file_name = self.sheet_name+".html"
        file.to_html(html_file_name)





