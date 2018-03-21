import os
""" This methos will goto the folder User and check wheather any xlsx file is present or not if present return the
 file name else return None """

def get_file_name():
        file_name=""
        list_file = []
        path = os.path.dirname(os.path.abspath(__file__)) + "\User"
        os.chdir(path)
        #Creat a list of all the file name present in the directory
        for (dirpath, dirnames, filenames) in os.walk(path):
            list_file.extend(filenames)
            break
        index = 0

        #It will check for xlsx file extension
        while index < len(list_file):
            if "xlsx" in list_file[index]:
                file_name = list_file[index]
                break
            index+=1

        #will check wheather loop is break by break statment or by condition become false
        if index == len(list_file):
            return None
        else:
            return file_name
