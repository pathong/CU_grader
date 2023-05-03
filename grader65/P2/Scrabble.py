s1 = "AEILNORSTU"
s2 = "DG"
s3 = "BCMP"
s4 = "FHVWY"
s5 = "K"
s8 = "JX"
s10 ="QZ"

words = input().strip().split()

rank = []
for word in words:
    score = 0
    for w in word:
        if w in s1: score += 1
        elif w in s2: score += 2
        elif w in s3: score += 3
        elif w in s4: score += 4
        elif w in s5: score += 5
        elif w in s8: score += 8
        elif w in s10: score += 10
    rank.append([-score, word, [word, str(score)]])
rank.sort()

for r in rank:
    print(" ".join(r[2]))


