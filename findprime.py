def findprime(r):
    for a in range(2,r+1):
        #k = 0
        for i in range(2,a//2):
            if a % i == 0:
                #k=k+1
                #if k<=0:
                    print(a)
                    break

findprime(13)