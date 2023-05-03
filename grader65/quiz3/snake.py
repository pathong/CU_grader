partys = dict()
par_order = list()
votes = dict()

## input
party_num = int(input())
for _ in range(party_num):
    party = input().strip()
    partys[party] = list()
    par_order.append(party)

people_num = int(input())
for i in range(people_num):
    pe,pa = input().strip().split()
    partys[pa].append(pe)

vote_num = int(input())
for _ in range(vote_num):
    pe,v = input().strip().split()
    votes[pe] = v

## count votes
for party in par_order:
    ## count vote
    vote_count = {'Y':0,'N':0,'X':0}
    for name,vote in votes.items():
        if name in partys[party]:
            vote_count[vote] += 1

    ## Inconclusive
    max_vote_c = max(list(vote_count.values()))
    if list(vote_count.values()).count(max_vote_c) > 1:
        print(party)
        print('Inconclusive')
        continue
    
    ## Get maxvote
    max_vote = ''
    for v,c in vote_count.items():
        if c == max_vote_c: max_vote = v

    ## get snake 
    snakes = []
    for p in partys[party]:
        if p not in votes.keys(): continue
        if votes[p] != max_vote: snakes.append(p)

    print(party)
    snakes.sort()
    print( ', '.join(snakes) if len(snakes) > 0 else 'No cobra')











