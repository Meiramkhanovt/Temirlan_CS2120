text ="I love mini oreo and semi colons"
text1=text.split()
for letter in text1:
    if letter[len(letter)-1]=="I" or letter[len(letter)-1]=="i":
        print(letter)
    