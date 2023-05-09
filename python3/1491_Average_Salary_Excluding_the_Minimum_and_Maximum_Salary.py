# 方法1.
class Solution:
    def average(self, salary: List[int]) -> float:
        total = 0
        count = 0
        for i in salary:
            if i != max(salary) and i != min(salary):
                total += i
                count += 1

        return total / count

# 方法2.
class Solution:
    def average(self, salary: List[int]) -> float:
        salary = sorted(salary)
        return sum(salary[1:-1]) / (len(salary) - 2)

# 方法 3.
class Solution:
    def average(self, salary: List[int]) -> float:
        return (sum(salary) - max(salary) - min(salary)) / (len(salary) - 2)
