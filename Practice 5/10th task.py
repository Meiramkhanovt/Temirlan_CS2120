import imp


import string
text = "The main gate creaks and groans. " '"' "I saw the SuperShell in the back. What" "'" "s she wear, medium or large?"'" "'"Large"'", I say, opening both eyes. There'"'s a contest: Whoever has the most sales gets to take home any coat in the store. When Richard asked me what I was going to do if I won, I told him that when I won I was going to give one of the SuperShell parkas to my mother. Richard frowned but said that was honorable. I said that yeah, it was. The SuperShells are the most expensive coats we have this season: down-filled lofted exterior with a water-repellent finish, zip vents to keep the thing breathable, elastic hem plus faux fur on the hood for a luxurious touch. I know Richard would have me choose literally anything else. That'"'s half of why I chose it. I set it aside in the back. It'"'s the only large we'"'ve got due to a shipment glitch. Nobody will touch it because I'"'m me."

for word in text.split():
    if (word.islower()):
        text=string.capwords(text)

print(text)