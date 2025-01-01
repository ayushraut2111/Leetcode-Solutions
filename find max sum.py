
if __name__=="__main__":
    print("inside main")

    s = "011101"

    count_1=s.count("1")
    count_0=s.count("0")
    
    print(count_0,count_1)

    for i in range(len(s)):
        left_string=s[:i+1]
        right_string=s[i+1:]
        print(left_string,right_string)