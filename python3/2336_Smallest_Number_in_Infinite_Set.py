class SmallestInfiniteSet:

    def __init__(self):
        self.values = set()
        

    def popSmallest(self) -> int:
        if len(self.values) == 0:
            self.values.add(1)
            return 1
        else:
            num = 0
            # 如果 values 包含了從 1 ~ n 那 SmallestinfiniteSet 的最小值一定是 n+1
            if max(self.values) == len(self.values):
                num = max(self.values) + 1
            else:
                # 如果 values 是 1,2,...X(缺失)...n-1,n
                # 那最小值一定是缺失部分的最小值
                for i in range(1, max(self.values) + 1):
                    if i not in self.values:
                        num = i
                        break
            self.values.add(num)
            return num
            

        

    def addBack(self, num: int) -> None:
        if num in self.values:
            self.values.remove(num)

        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
