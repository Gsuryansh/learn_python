def hamming(s1,s2):
    if len(s1) != len(s2):
        raise ValueError("Not defined - unequal lenght sequences")
    return sum(c1 != c2 for c1,c2 in zip(s1,s2))
print (hamming("suryansh","saryanas"))