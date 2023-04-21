class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if people is None:
            return 0

        people = sorted(people)

        i = 0
        j = len(people) - 1

        result = 0

        # 每艘船最多坐兩個人, 要最少的船，那就最輕和最重搭配看看
        # 如果兩人體重小於限重，就能一起搭
        while i <= j:
            result += 1
            if people[i] + people[j] <= limit:
                i += 1
            print(people[i], people[j])
            j -= 1

        return result
