input_string = "aAbBcCFDfdertRtYHTJ"
output_string = ""

for char in input_string:
    if ord(char)>=97:
        output_string = output_string +chr(ord(char)-32)

    else:
        output_string = output_string +chr(ord(char)+32)

print(output_string)