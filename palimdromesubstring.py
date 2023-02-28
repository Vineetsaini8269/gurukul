s="abccbhk"
l=[]

for x in range(2,len(s)+1):
    min=0
    while(min+x)<len(s)+1:
        if s[min:(min+x)]==s[min:(min+x)][::-1]:
            l.append(s)
            min+=1
            print(l)