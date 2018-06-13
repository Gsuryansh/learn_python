seat_nos = [int(i) for i in raw_input("Please enter the seat number").split()]

for i in range(len(seat_nos)):
    if int(seat_nos[i])%6 == 1 or int(seat_nos[i])%6 == 0:
        print("{} is window seat".format(seat_nos[i]))
    elif int(seat_nos[i])%3 == 1 or int(seat_nos[i])%3 == 0:
        print("{} is corner seat".format(seat_nos[i]))
    else:
        print("{} is middle seat".format(seat_nos[i]))
