def check_digit(n):

    k = 0
    for i in range(12):
          k += (13-i)*int(n[i])
    return (11 - (k % 11)) %10

exec(input())
