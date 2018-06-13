# import argparse
#
# parser  = argparse.ArgumentParser(description="Learning command line argument")

# import datetime
#
# hour = datetime.datetime.now().time().hour
# minute = datetime.datetime.now().time().minute
# second = datetime.datetime.now().time().second
# fianltime = hour*3600 + minute*60 + second + 30*60
#
# hour = fianltime/3600
# minute = (fianltime%3600)/60
# second = (fianltime%3600)%60
#
# time = str(hour)+":"+str(minute)+":"+str(second)
# print(time)


from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument("-f", "--file", dest="filename",
                    help="write report to FILE", metavar="FILE")