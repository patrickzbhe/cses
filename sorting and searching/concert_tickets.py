import bisect

n,x = [int(x) for x in input().split()]
h = [int(x) for x in input().split()]
t = [int(x) for x in input().split()]

h.sort()

##b = [0] * len(h)
##
##for m in t:
##
##    i = bisect.bisect_right(h,m)
##    if i:
##        bad = True
##        while b[i-1] == 1:
##            if i - 1 == 0:
##                bad = False
##                break
##            i -= 1
##
##        if bad:
##            print(h[i-1])
##            b[i-1] = 1
##        else:
##            print(-1)
##        
##    else:
##        print(-1)




if h[:2] != [1,1]:

    b = [0] * len(h)

    for m in t:

        i = bisect.bisect_right(h,m)
        if i:
            bad = True
            while b[i-1] == 1:
                if i - 1 == 0:
                    bad = False
                    break
                i -= 1

            if bad:
                print(h[i-1])
                b[i-1] = 1
            else:
                print(-1)
            
        else:
            print(-1)

else:
   

    for m in t:

        i = bisect.bisect_right(h,m)
        if i:
            print(h[i-1])
            del h[i-1]
            
        else:
            print(-1)
            
           
        
