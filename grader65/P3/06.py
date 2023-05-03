n = int(input())
actor_movie = dict()
for _ in range(n):
    # input

    t, s1,s2 = input().split(',')
    t = t.strip()
    s1 = s1.strip()
    s2 = s2.strip()

    li = [s1,s2]
    for s in li:

        if s not in actor_movie.keys():
            actor_movie[s] = list()

        actor_movie[s].append(t)



stars=  [e.strip() for e in input().split(',')]
for star in stars:
    if star in actor_movie:
        print(star,'->', ", ".join(actor_movie[star]))
    else:
        print(star, '->', 'Not found')

