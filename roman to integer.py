def intToRoman(n: int):
    num = [1, 4, 5, 9, 10, 40, 50, 90,
        100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
        "L", "XC", "C", "CD", "D", "CM", "M"]
    if n in num:
        return sym[num.index(n)]
    s=''
    while n>0:
        if n in num:
            s+=sym[num.index(n)]
            break
        i=0
        while i<len(num) and n>num[i]:
            i+=1
        if i>len(num):
            s+='M'
            n-=1000
        else:
            n-=num[i-1]
            # print(n)
            s+=sym[i-1]
        # print(n)
    return s
        


    


print(intToRoman(4990))
