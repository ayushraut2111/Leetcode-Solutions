def maximumSwap(num: int) -> int:
       if num<=10:
           return num
       a = [int(x) for x in str(num)]
       temp=a[:]
       temp.sort(reverse=True)
       if a==temp:
           return int("".join(map(str, a)))
       for i in range(len(a)):
           if a[i]!=temp[i]:
               j=len(a)-1
               while temp[i]!=a[j]:
                   j-=1
               x=a[i]
               a[i]=a[j]
               a[j]=x
               p= int("".join(map(str, a)))
               return p
       p= int("".join(map(str, a)))
       return p
    
print(maximumSwap(967))