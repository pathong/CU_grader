s = input()
es1 = 'sx'
es2 = 'ch'
vowel = 'aeiou'
if s[-1] in es1 or s[-2:] == es2:
    s += "es"
elif s[-1] == "y" and s[-2] not in vowel:
    s = s[:-1] + "ies"
else:
    s += "s"

print(s)
