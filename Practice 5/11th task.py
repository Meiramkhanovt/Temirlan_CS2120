text = input() 
a=0
b=0
for word in text:
    if word == 'n' or word == "N":
        a += 1
    elif word != 'n' and word!="N":
        if b < a:
            b = a
            a = 0
    else : break
            
text=text.replace("!", ".")
print(b)
print(text)
