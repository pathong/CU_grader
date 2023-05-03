s = input().split()
a = ""
u = "abcdefghijklmnopqrstuywzyz1234567890"
for i in range(len(s)):
    _s = ""
    for c in s[i]:
        if c in u.lower() or c in u.upper():
            _s +=c 
    s[i] = _s[0].upper() + _s[1:].lower()

s = "".join(s)
s = s[0].lower() + s[1:]
print(s)
