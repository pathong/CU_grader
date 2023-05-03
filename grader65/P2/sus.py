p1 = 'color.txt' 
p2 = 'song.txt'

f_color = open(p1,'r')
f_song = open(p2,'r')

## file -> list of color
color_list = []
for l in f_color:
    if len(l) == 0: continue
    color_list += l.split()



## file -> list of song
li_song = []
for l in f_song:
    li_song.append(l.strip())


## loop through color list
for color in color_list:

    ## loop through each song
    for x in range(len(li_song)):
        l = li_song[x]

        if color.lower() not in l.lower(): continue
        newline = ""
        i = 0
        ## loop check each chunk in song's line
        while True:
            ## if chunk same as color -> change line
            if l[i:i+len(color)].lower() == color.lower():
                newline += "<" + color.lower() + ">"+l[i:i+len(color)]+"</>"
                ## skip index
                i+=len(color)
            ## if not found
            else:
                newline += l[i]
                i+=1
            ## break condition
            if i >= len(l):break

        ## change in list
        li_song[x] = newline

## print
for l in li_song:
    print(l)


