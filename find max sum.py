
if __name__=="__main__":
    print("inside main")

    s = "011101"

    count_1=s.count("1")
    count_0=s.count("0")
    
    print(count_0,count_1)
    max_sum=0

    for i in range(len(s)):
        left_string=s[:i+1]
        right_string=s[i+1:]

        if len(left_string)==0 or len(right_string)==0:
            continue

        max_sum=max(max_sum,left_string.count("0")+right_string.count("1"))
    print(max_sum)