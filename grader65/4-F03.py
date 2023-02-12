def grade_mcq(sol,ans):
    if len(sol) != len(ans) : return -1
    s = 0
    for i in range(len(sol)):
        if sol[i] == ans[i] : s += 1

    return s

exec(input())
