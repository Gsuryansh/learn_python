letter={}
a="suryansh"
for i in a:
    if i in letter:
        letter[i]=letter[i]+1
    else:
        letter[i]=1
print(letter.items())

