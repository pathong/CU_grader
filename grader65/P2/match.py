def match(word, pattern, include_chars, exclude_chars):
    if len(word) != len(pattern) : return False 

    for i in range(len(word)):
        if pattern[i] != "?" and pattern[i] != word[i] : return False

    for i in range(len(pattern)):
        if pattern[i] == "?":
            if word[i] in exclude_chars: return False


    disableIndex = []
    for inc in include_chars:
        for j in range(len(pattern)):
            if j not in disableIndex and pattern[j] == "?" and word[j] == inc:
                disableIndex.append(j)
                break
    if len(include_chars) != len(disableIndex) : return False
                
    return True


print(match("MACMA", "M?C??", "MAA", ""))
print(match("MACMA", "M?C??", "AM", ""))
print(match("MACMA", "M?C??", "", ""))
print(match("MACMA", "M?C??", "", "CPE"))
print(match("MACMA", "?????", "AAMM", "OK"))
print(match("MACMA", "MACMA", "", "MACMA"))
print(match("MACMA", "M?C??", "AAA", ""))
print(match("MACMA", "M?C??", "MAX", ""))
print(match("MACMA", "M?C??", "C", ""))
print(match("MACMA", "M?C??", "", "MX"))
print(match("MACMA", "M?C???", "", ""))
print(match("MACMA", "M?C?", "", ""))

