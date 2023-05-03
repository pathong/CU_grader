key = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz','0': " "}


def text2keys(text):
    key_li = []
    for t in text:
        if t == " ":
            key_li.append("0")
            continue

        if not t.isalpha():continue
        for k,v in key.items():
            if t.lower() in v:
                
                key_li.append(k*(v.find(t.lower())+1))

    return " ".join(key_li)
def keys2text(keys):
    key_li = keys.split()
    word = ""
    for  k in key_li:
        word += key[k[0]][len(k)-1]
    return word

exec(input())
