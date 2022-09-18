text ="I love mini oreo, ananas and baunti"
text1=text.split()
for letter in text1:
    if letter[len(letter)-1]=="I" or letter[len(letter)-1]=="i":
        print(letter)
    elif letter[0]=="a" or letter[0]=="A":
        print(letter)
    