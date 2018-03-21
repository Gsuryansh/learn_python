import json


with open('constants_auto.json', 'r+') as f:
    data = json.load(f)
    # data['terminal']['tid'] = "12345678"
    # f.seek(0)
    # json.dump(data, f,indent=4)
    print(data)
