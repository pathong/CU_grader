result = input().strip()
target = int(input())
i = 0

total_score = 0

curr_f=1
score_frame = 0
score = 0

n = 0
for i in range(len(result)):
    r = result[i]
    if r == "X":
        score_frame += 10
        if result[i+1] == "X": score_frame += 10
        else: score_frame += int(result[i+1])

        if result[i+2] == "/": score_frame += 10-int(result[i+1])
        elif result[i+2] == "X": score_frame += 10
        else: score_frame += int(result[i+2])

        # print("frame {} : {}".format(curr_f, score_frame))
        score += score_frame
        if curr_f == target:
            print(score_frame)
            break
        curr_f +=1
        score_frame = 0
        n = 0 
    elif r == "/":
        score_frame += 10-int(result[i-1])
        if result[i+1] == "X": score_frame += 10
        else: score_frame += int(result[i+1])

        # print("frame {} : {}".format(curr_f, score_frame))
        score += score_frame
        if curr_f == target:
            print(score_frame)
            break
        curr_f +=1
        score_frame = 0
        n = 0
    else:
        n += 1
        score_frame += int(r)
        if n == 2:
            # print("frame {} : {}".format(curr_f, score_frame))
            score += score_frame
            if curr_f == target:
                print(score_frame)
                break
            curr_f +=1
            score_frame =0
            n = 0

    if curr_f == 10:
        for j in range(i+1,len(result)):
            if result[j] == "X": score_frame +=10
            elif result[j] == "/": score_frame += 10-int(result[j-1])
            else: score_frame += int(result[j])
        # print("frame {} : {}".format(curr_f, score_frame))
        score += score_frame
        if curr_f == target:
            print(score_frame)
        break
        
if target not in range(1,11) : print(score)



            







    







