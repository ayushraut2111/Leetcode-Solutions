# https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/
import random
class RandomizedCollection:

    def __init__(self):
        self.mp={}
        self.ls=[]
        

    def insert(self, val: int) -> bool:
        if val in self.mp:
            self.mp[val]+=1
            self.ls.append(val)
            return False
        else:
            self.mp[val]=1
            self.ls.append(val)
            return True
        

    def remove(self, val: int) -> bool:
        if val in self.mp:
            self.mp[val]-=1
            self.ls.remove(val)
            if self.mp[val]==0:
                del self.mp[val]
            return True
        return False
        

    def getRandom(self) -> int:
        return random.choice(self.ls)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()