def countNumbersWithUniqueDigits(n):
        count=0
        if n==0:
            return 1
        if n==1:
            return 10
        for i in range(10,(10**n)):
            a=str(i)
            p=list(map(int,a))
            if len(set(p))==len(a):
                # print(set(p),a)
                count+=1
        return count+10

print(countNumbersWithUniqueDigits(8))