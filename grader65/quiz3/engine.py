
def frequency(body, word):
    li = body.split()
    return li.count(word)/len(li)
def unique(body):
    return 1/len(set(body.split()))

n = int(input())
paper = dict()
for _ in range(n):
    header = input()
    body = input()
    paper[header] = body

while True:
    max_score = 0
    curr_header = ""
    search = input()
    if search == '-1': break

    for k,v in paper.items():
        score = frequency(v,search) * unique(v)
        if score > max_score:
            max_score = score
            curr_header = k
    if max_score == 0:
        print('NOT FOUND')
    else:
        print(curr_header)





    

