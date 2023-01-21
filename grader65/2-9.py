def check_digit(n):

    def N(i)->int:
        return int(n[i])
    k = 0
    for i in range(12):
          k += (13-i)*N(i)
    return (11 - (k % 11)) %10

exec(input())
