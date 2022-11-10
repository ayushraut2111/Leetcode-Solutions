# https://leetcode.com/problems/maximum-69-number/submissions
def maximum69Number (num: int) -> int:
        if num<=10:
            return 9
        a = [int(x) for x in str(num)]
        for i in range(len(a)):
            if a[i]==6:
                a[i]=9
                break
        p= int("".join(map(str, a)))
        return p
print(maximum69Number(9969))