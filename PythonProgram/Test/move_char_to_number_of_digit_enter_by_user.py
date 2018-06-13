string = "AYZ12349*()abgc"

input_int = 200

output_string = ""

for value in string:
    if ord(value)>=ord("A") and ord(value)<=ord("Z"):
        input_int = input_int%26
        if ord(value) + input_int <= ord("Z"):
            output_string = output_string + chr(ord(value)+input_int)

        else:
            difference = (ord(value)+input_int) - ord("Z")
            output_string = output_string + chr(ord("A")-1+difference)

    elif ord(value) >= ord("a") and ord(value) <= ord("z"):
            input_int = input_int % 26
            if ord(value) + input_int <= ord("z"):
                output_string = output_string + chr(ord(value) + input_int)

            else:
                difference = (ord(value) + input_int) - ord("z")
                output_string = output_string + chr(ord("a") - 1 + difference)
    elif ord(value) >= ord("0") and ord(value) <= ord("9"):
            input_int = input_int % 10
            if ord(value) + input_int <= ord("9"):
                output_string = output_string + chr(ord(value) + input_int)

            else:
                difference = (ord(value) + input_int) - ord("9")
                output_string = output_string + chr(ord("0") - 1 + difference)
    else:
        output_string = output_string + value


print(output_string)



