import os

class Directory(object):
    def __init__(self):
        self.path = (os.path.dirname(os.path.abspath(__file__)))

    def change_working_directory(self):
        print(os.getcwd())
        os.chdir("..")
        print(os.getcwd())


    def creat_directory(self):
        if self.path.find("Report") == -1:
            self.change_working_directory()
        if not os.path.exists(self.path+"\Report"):
                os.makedirs("Report")
        path = os.path.dirname(os.path.abspath(__file__)) + "\Report"
        os.chdir(path)
#print(os.path.dirname(os.path.abspath(__file__)))print(os.getcwd())
