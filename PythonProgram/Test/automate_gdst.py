import os
count = 1
dir_name = os.path.dirname(os.path.realpath(__file__))
path_gdst = os.path.join(dir_name, 'TransactionAcquirerRules.gdst')
temp_gdst = os.path.join(dir_name, 'temp.txt')
print(temp_gdst)
with open(temp_gdst, 'w') as temp:
    with open(path_gdst) as f:
        for value in f:
            if "MerchantIdEnums" in value:
                if count == 1:
                    temp.write(value)
                    count = count + 1
                else:
                    index = value.find("MerchantIdEnums")
                    string = value.replace(value[index:45], "MerchantIdEnums." + "AMer0052")
                    temp.write(string)
            else:
                temp.write(value)
os.remove(path_gdst)
os.rename(temp_gdst, path_gdst)


