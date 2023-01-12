def str2hms(hms_str):
 t = hms_str.split(':')
 return int(t[0]),int(t[1]),int(t[2])
def hms2str(h,m,s):
 return ('0'+str(h))[-2:] + ':' + \
 ('0'+str(m))[-2:] + ':' + \
 ('0'+str(s))[-2:]

def to_sec(h,m,s):
    return h*60*60 + m*60 + s
def to_hms(s):
    dh = s // (60*60)
    s -= dh * 60*60
    dm = s // 60
    s -= dm*60
    ds = s 
    
    return dh, dm, ds
def diff(h1,m1,s1,h2,m2,s2):
    dt = to_sec(h2,m2,s2) - to_sec(h1,m1,s1)
    return to_hms(dt) 

def main():
    hms_start = input()
    hms_end = input()
    h1,m1,s1 =str2hms(hms_start)
    h2,m2,s2 =str2hms(hms_end)
    dh,dm,ds = diff(h1,m1,s1,h2,m2,s2)
    print(hms2str(dh,dm,ds))





exec(input()) # DON'T remove this line
