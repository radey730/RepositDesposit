#should return m is a consonant, u is a vowel, y is a y; 'y' 'vowel' and 'consosant' shud be variablesmust f string

letter1 = 'm'
letter2 = 'u'
letter3 = 'y'

vowel = 'aeiou'
consonant = 'bcdfgjklmnpqrstvwxz'
y = 'y'

if letter1 in vowel:
    print(f"{letter1} is a vowel")
elif letter1 in consonant:
     print(f"{letter1} is a consonant")
else:
    print(f"{letter1} don't go down")
    
    
if letter2 in vowel:
    print(f"{letter2} is a vowel")
elif letter2 in consonant:
    print(f"{letter2} is a consonant")
else:
     print(f"{letter2} don't go down")
     
     
if letter3 in vowel:
    print(f"{letter3} is a vowel")
elif letter3 in consonant:
    print(f"{letter3} is a consonant")
else:
     print(f"{letter3} is a y")
   