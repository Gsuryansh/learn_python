import requests
import urllib3
from datetime import datetime
import time



urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

current_time = []
utid_specific_file = []
# now = datetime.now()
# print(now.strftime("%Y-%m-%d %H:%M:%S"))

post_result = requests.post("https://192.168.0.97:5454/emi-integration-api/jobs/csv/launch/L0031802", verify = False)
time.sleep(2)
get_result = requests.get("https://192.168.0.97:5454/emi-integration-api/jobs/mapping/file/list",verify = False)
time.sleep(3)
for data in get_result.json():
    if "L0031802" in data["fileName"]:
        utid_specific_file.append({"fileName":data["fileName"],"creationTime":data["creationTime"]})
for utid_data in utid_specific_file:
    date_time = datetime.strptime(utid_data["creationTime"],'%d-%b-%Y %H:%M:%S')
    current_time.append(date_time)
sorted_time_list = sorted(current_time,reverse=True)
file_name = ''
for value in utid_specific_file:
    temp = datetime.strptime(value["creationTime"],'%d-%b-%Y %H:%M:%S')
    if temp == sorted_time_list[0]:
        file_name = value['fileName']
final_file = requests.get("https://192.168.0.97:5454/emi-integration-api/jobs/download/file/"+file_name,verify = False,stream=True)
time.sleep(2)
print(final_file.text)
with open(file_name,'w') as csv_file:
    csv_file.write(final_file.text)

