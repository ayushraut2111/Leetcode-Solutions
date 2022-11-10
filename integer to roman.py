def romanToInt(s: str) -> int:
    roman = {}
    roman['I'] = 1
    roman['V'] = 5
    roman['X'] = 10
    roman['L'] = 50
    roman['C'] = 100
    roman['D'] = 500
    roman['M'] = 1000
    ans=0
    for i in range(len(s)-1):
        if roman[s[i]]<roman[s[i+1]]:
            ans-=roman[s[i]]
        else:
            ans+=roman[s[i]]
    ans+=roman[s[len(s)-1]]
    return ans

print(romanToInt('VIX'))