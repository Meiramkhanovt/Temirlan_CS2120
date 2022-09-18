text ="I love (mini oreo and semi colons) you"
a=text.find("(")+1
b=text.find(")")
text1=text[a: b]
print(text1)