def cardLuhnChecksumIsValid(card_number):
    """ checks to make sure that the card passes a luhn mod-10 checksum """

    sum = 0
    num_digits = len(card_number)
    oddeven = num_digits & 1

    for count in range(0, num_digits):
        digit = int(card_number[count])

        if not (( count & 1 ) ^ oddeven ):
            digit = digit * 2
        if digit > 9:
            digit = digit - 9

        sum = sum + digit

    return ( (sum % 10) == 0 )

if __name__ == "__main__":
    bin_range = "622018"
    a = [format(item, "05d") for item in xrange(100000)]
    b = [format(item, "05d") for item in xrange(100000)]

    counter = 0
    for i in a:
        for j  in b:
            card_number = bin_range + str(i) + str(j)

            lhun_chk_sts = cardLuhnChecksumIsValid(card_number)
            if lhun_chk_sts:
                counter = counter + 1
                print "Valid card: {}".format(card_number)

                if counter >= 10:
                    exit(0)