# https://leetcode.com/problems/min-stack
class MinStack:

    def __init__(self):
        self.st=[]
        self.mini=None

    def push(self, val: int) -> None:
        if len(self.st)==0:
            self.mini=val
            self.st.append(val)
        elif val<=self.mini:
            self.st.append(2*val-self.mini)
            self.mini=val
        else:
            self.st.append(val)
        
        

    def pop(self) -> None:
        x=self.st.pop()
        if x<=self.mini:
            res=self.mini
            self.mini=2*self.mini-x

    def top(self) -> int:
        t=self.st[-1]
        if t<=self.mini:
            return self.mini
        return t

    def getMin(self) -> int:
        return self.mini


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()