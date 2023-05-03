class Group():

    def __init__(self,ally:set) -> None:
        self.ally = ally 
        self.enemy = set()
        

a_li = []
e_li = []
while True:
    ## get input
    inp = input().split()
    if len(inp) <= 1:break
    mode = inp[0]
    li = inp[1:]
    if mode == 'Ally':
        cur_al = Group(set(li))
        a_li.append(cur_al)
    if mode == 'Enemy':

        curr = ''
        ene = ''
        for ind in range(len(li)):
            if ind == 0:
                curr = li[ind]
                e = li[1]
            elif ind == 1:
                curr = li[ind]
                e = li[0]

            ## find curr in Group
            cur_obj = None

            alreadyinGroup = False
            for a in a_li:
                if curr in a.ally:
                    alreadyinGroup = True
                    cur_obj = a
            if not alreadyinGroup:
                cur_obj = Group(set(curr))
                a_li.append(cur_obj)
            
            ## append enemy into set


                




