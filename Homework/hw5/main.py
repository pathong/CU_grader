import csv
from re import M
fn = open('athlete_events_2000-2016_cl.csv', 'r', encoding='utf-8-sig') 
data = list(csv.reader(fn, delimiter = ','))
fn.close()

fn = open('athlete_events_mock.csv', 'r', encoding='utf-8-sig') 
data_mock = list(csv.reader(fn, delimiter = ','))
fn.close()

def convert_to_dict(data):
    athletes_by_Year_NOC = {}
    for d in data[1:]:
        year = d[9]
        noc = d[7]
        if year not in athletes_by_Year_NOC.keys(): athletes_by_Year_NOC[year] = dict()
        if noc not in athletes_by_Year_NOC[year].keys(): athletes_by_Year_NOC[year][noc] = []
        inp = dict()
        head = data[0]
        for i in range(len(head)):
            inp[head[i]] = d[i]
        athletes_by_Year_NOC[year][noc].append(inp)

    return athletes_by_Year_NOC

# d = convert_to_dict(data_mock)
# print(d)

# d = convert_to_dict(data)
# print(len(d['2000']['THA']))
# for i in range(5):
    # print(d['2000']['THA'][i])

def get_medals_by_team(athletes_by_Year_NOC, year):
    ath_noc = athletes_by_Year_NOC[year]
    medal_summary = dict()
    for noc,li_ath in ath_noc.items():
        g = 0
        s = 0
        b = 0
        for ath in li_ath:
            medal = ath['Medal']
            if medal == 'NA': continue
            elif medal == 'Bronze': b += 1
            elif medal == 'Silver': s += 1
            elif medal == 'Gold': g += 1
        medal_summary[noc] = (g,s,b)
    return medal_summary

# d = convert_to_dict(data)
# m = get_medals_by_team(d, '2000')
# print(len(m))
# print(m)

def get_top_five(medals):
    li = []
    top_five = []
    for k,v in medals.items():
        li.append([-v[0],-v[1],-v[2],k])
    li.sort()
    for l in li:
        if len(top_five) >= 5 and (top_five[4][1],top_five[4][2],top_five[4][3]) != (-l[0],-l[1],-l[2]):break
        
        top_five.append((l[3],-l[0],-l[1],-l[2]))

    return top_five

# d = convert_to_dict(data)
# m = get_medals_by_team(d, '2000')
# print(get_top_five(m))

def get_medals_trend(athletes_by_Year_NOC,NOC,start,end):
    li = []
    for year in range(start,end+1):
        if str(year) not in athletes_by_Year_NOC.keys(): continue
        medals_summary = get_medals_by_team(athletes_by_Year_NOC,str(year))
        if NOC not in medals_summary.keys(): continue
        medals = medals_summary[NOC]
        li.append((str(year),)+medals)
    return li


d = convert_to_dict(data)
print('USA')
print(get_medals_trend(d, 'USA', 2001, 2015))
print('THA')
print(get_medals_trend(d, 'THA', 2000, 2016))


        




