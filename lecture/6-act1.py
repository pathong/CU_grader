def is_undergrad(sid): return sid[2] in "034"
def get_faculty(sid):
    fa = sid[-2:]
    if fa == "21": return "ENG"
    elif fa == "22" :return "ART"
    elif fa == "23" :return "SCI"
    else: return "OTHER"
def get_status(sid): return ["U" if is_undergrad(sid) else "G", get_faculty(sid)]

exec(input())
