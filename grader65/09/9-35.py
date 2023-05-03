class Student():
    prop = list() 
    def __init__(self,prop:list) -> None:
        self.prop = prop
    def isMe(self,check:list):
        t_c = 0
        for c in check:
            if c in self.prop:  
                t_c += 1
        return True if len(check) == t_c else False 



li = []
n = int(input())
for _ in range(n):
    li.append(Student(input().strip().split()))
check = input().split()
ans = []
for s in li:
    if s.isMe(check): ans.append(" ".join(s.prop))

for a in sorted(ans):
    print(a)



AFJ Dog 95 EE
AUI Dog 95 ME
BECX Dog 90 CHE
BNOR Dog 110 ENV
BPQE Dog 105 SV
CFU Dog 105 PE
DBRLI Dog 105 CE
EDA Dog 96 PE
FOMKM Dog 92 CP
FQRH Dog 95 CP
FQWT Dog 105 ENV
GPZ Dog 96 PE
GST Dog 93 SV
ICEUS Dog 105 CP
IXRC Dog 99 MT
KBFDD Dog 96 CE
MDRGX Dog 105 PE
MOE Dog 108 PE
NFRYG Dog 94 MT
OUQ Dog 93 CE
PKMWH Dog 109 CP
QCAZ Dog 95 CHE
QQGJW Dog 94 PE
SGEZ Dog 95 SV
SKSAV Dog 100 IE
TZP Dog 96 ME
WQGEB Dog 99 IE
WUFRS Dog 107 ME
YVO Dog 102 ME
ZAV Dog 96 PE

AFJ Dog 95 EE
AUI Dog 95 ME
BECX Dog 90 CHE
BNOR Dog 110 ENV
BPQE Dog 105 SV
CFU Dog 105 PE
DBRLI Dog 105 CE
Dog N 110 PE
EDA Dog 96 PE
FOMKM Dog 92 CP
FQRH Dog 95 CP
FQWT Dog 105 ENV
GPZ Dog 96 PE
GST Dog 93 SV
ICEUS Dog 105 CP
IXRC Dog 99 MT
KBFDD Dog 96 CE
MDRGX Dog 105 PE
MOE Dog 108 PE
NFRYG Dog 94 MT
OUQ Dog 93 CE
PKMWH Dog 109 CP
QCAZ Dog 95 CHE
QQGJW Dog 94 PE
SGEZ Dog 95 SV
SKSAV Dog 100 IE
TZP Dog 96 ME
WQGEB Dog 99 IE
WUFRS Dog 107 ME
YVO Dog 102 ME
ZAV Dog 96 PE
